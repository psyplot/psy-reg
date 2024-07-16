"""Test file for the psy-reg plotters."""

# SPDX-FileCopyrightText: 2021-2024 Helmholtz-Zentrum hereon GmbH
# SPDX-FileCopyrightText: 2020-2021 Helmholtz-Zentrum Geesthacht
# SPDX-FileCopyrightText: 2016-2024 University of Lausanne
#
# SPDX-License-Identifier: LGPL-3.0-only


import subprocess as spr
import sys
import unittest

import matplotlib.pyplot as plt
import numpy as np
import psyplot.data as psyd
import xarray as xr

from psy_reg.plotters import DensityRegPlotter, LinRegPlotter

# check if the seaborn version is smaller than 0.8 (without actually importing
# it), due to https://github.com/mwaskom/seaborn/issues/966
# If so, disable the import of it when import psyplot.project
sns_version: str
try:
    sns_version = spr.check_output(  # type: ignore
        [sys.executable, "-c", "import seaborn; print(seaborn.__version__)"]
    )
except spr.CalledProcessError:  # seaborn is not installed
    sns_version = ""
else:
    sns_version = sns_version.decode("utf-8")  # type: ignore


class LinRegPlotterTest(unittest.TestCase):
    default_slope = 3
    default_intercept = 2
    default_n = 500

    plotter_cls = LinRegPlotter

    def tearDown(self):
        plt.close("all")

    @property
    def plot_data(self):
        return self.plotter.plot_data[0]

    @property
    def fit_plot_fmt(self):
        return self.plotter.plot

    @classmethod
    def define_data(
        cls, slope=None, intercept=None, scatter=0.1, n=None, **kwargs
    ):
        """Set up the data

        Parameters
        ----------
        slope: float
            The slope of the data. If None, defaults to the
            :attr:`default_slope` attribute
        intercept: float
            The y-value for x==0. If None, defaults to the
            :attr:`default_intercept` attribute
        scatter: float
            The range for the random noise. Random noise will be like
            ``y * rand * scatter`` where rand is a normally random number
            between [-1, 1]
        n: int
            The number of data points. If None, defaults to the
            :attr:`default_n` attribute

        Returns
        -------
        xarray.DataArray
            The array with the x- and y-data that can serve as an input for
            the :class:`psyplot.plotter.linreg.LinRegPlotter`
        """
        if slope is None:
            slope = cls.default_slope
        if intercept is None:
            intercept = cls.default_intercept
        if n is None:
            n = cls.default_n
        x = np.linspace(0, 10, n)
        y = intercept + slope * x
        y += y * np.random.randn(n) * scatter
        da = xr.DataArray(
            y, name="y", dims=("x",), coords={"x": xr.Variable(("x",), x)}
        )
        da.psy.base["v"] = da.x.variable
        return psyd.InteractiveList([da])

    @classmethod
    def define_curve_data(cls, a=None, scatter=0.1, n=None, **kwargs):
        """
        Set up the data

        This method uses the function

        .. math::

            y = a^2 * x * (1 - x)

        to generate data with a polynom of order 2.

        Parameters
        ----------
        a: float
            The parameter to use in the above equation
        scatter: float
            The range for the random noise. Random noise will be like
            ``y * rand * scatter`` where rand is a normally random number
            between [-1, 1]
        n: int
            The number of data points. If None, defaults to the
            :attr:`default_n` attribute

        Returns
        -------
        psyplot.data.InteractiveArray
            The array with the x- and y-data that can serve as an input for
            the :class:`psyplot.plotter.linreg.LinRegPlotter`
        """

        def func(x, a):
            return a * a * x * (1 - x)

        if a is None:
            a = 1.0434
        if n is None:
            n = cls.default_n
        x = np.linspace(0, 1, n)
        y = func(x, a)
        y += y * np.random.randn(n) * scatter
        da = psyd.InteractiveList(
            [
                xr.DataArray(
                    y,
                    name="y",
                    dims=("x",),
                    coords={"x": xr.Variable(("x",), x)},
                )
            ]
        )
        return da, func

    @classmethod
    def define_poly_data(cls, coeffs=[1, 2, 3], scatter=0.1, n=None, **kwargs):
        """
        Set up the data for a polynomial

        Parameters
        ----------
        coeffs: list of float
            The coefficients of the polynomial
        scatter: float
            The range for the random noise. Random noise will be like
            ``y * rand * scatter`` where rand is a normally random number
            between [-1, 1]
        n: int
            The number of data points. If None, defaults to the
            :attr:`default_n` attribute

        Returns
        -------
        psyplot.data.InteractiveArray
            The array with the x- and y-data that can serve as an input for
            the :class:`psyplot.plotter.linreg.LinRegPlotter`
        int
            The degree of the polynomial
        """
        if n is None:
            n = cls.default_n
        x = np.linspace(0, 1, n)
        y = np.poly1d(coeffs)(x)
        y += y * np.random.randn(n) * scatter
        da = psyd.InteractiveList(
            [
                xr.DataArray(
                    y,
                    name="y",
                    dims=("x",),
                    coords={"x": xr.Variable(("x",), x)},
                )
            ]
        )
        return da, len(coeffs) - 1

    def test_nonfixed_fit(self):
        """Test whether the fit works"""
        da = self.define_data()
        self.plotter = self.plotter_cls(da)
        data = self.plot_data
        self.assertGreater(data.rsquared, 0.8)

    def test_fix0(self):
        """Test with a fix point of 0"""
        da = self.define_data(intercept=0)
        self.plotter = self.plotter_cls(da, fix=0)
        data = self.plot_data
        self.assertEqual(data.intercept, 0)
        self.assertGreater(data.rsquared, 0.8)

    def test_fix1(self):
        """Test with a fix point at (0, 1)"""
        da = self.define_data(intercept=1)
        self.plotter = self.plotter_cls(da, fix=1)
        data = self.plot_data
        self.assertEqual(data.intercept, 1)
        self.assertGreater(data.rsquared, 0.8)

    def test_legend(self):
        self.test_nonfixed_fit()
        self.plotter.update(
            legendlabels="%(intercept)1.1f + %(slope)1.1f * x, "
            "R^2=%(rsquared)1.1f"
        )
        t = plt.gca().legend_.get_texts()[0].get_text()
        data = self.plot_data
        d = {
            "intercept": round(data.intercept, 1),
            "slope": round(data.slope, 1),
            "rsquared": round(data.rsquared, 1),
        }
        self.assertEqual(
            t, "%(intercept)s + %(slope)s * x, R^2=%(rsquared)s" % d
        )

    def test_ci(self):
        """Test whether the confidence interval is drawn"""
        self.test_nonfixed_fit()
        ax = self.plotter.ax
        err_fmt = self.plotter.error
        self.assertEqual(self.plot_data.shape[0], 3)
        self.assertTrue(hasattr(err_fmt, "_plot") and len(err_fmt._plot) >= 1)
        self.assertTrue(all(a in ax.collections for a in err_fmt._plot))

    def test_curve_fit(self):
        """Testing the fit of a polynom"""

        def test():
            da, func = self.define_curve_data()
            self.plotter = plotter = self.plotter_cls(da, fit=func)
            err = np.sqrt(plotter.fit.fits[0].pcov[0, 0])
            self.assertLess(err, 0.01)

        if sns_version and sns_version >= "0.8":
            # Test whether the warning is raised that the boundaries have
            # to be specified
            with self.assertWarnsRegex(RuntimeWarning, "boundaries"):
                test()
        else:
            test()
        self.plotter.update(param_bounds=[-1, 2])
        self.assertIsNotNone(self.plotter.p0.p0())

    def test_poly(self):
        """Testing the fit of a polynom"""
        da, deg = self.define_poly_data()
        self.plotter = self.plotter_cls(da, fit="poly%i" % deg)

    def test_2fits(self):
        """Test 2 different fits"""
        sequence = self.define_data()
        sequence.append(sequence[0].copy(True), new_name=True)
        plotter = self.plotter_cls(sequence, fit=["fit", "poly1"])
        self.assertIn("intercept", plotter.plot_data[0].attrs)
        self.assertNotIn("intercept", plotter.plot_data[1].attrs)
        self.assertIn("c1", plotter.plot_data[1].attrs)
        self.assertNotIn("c1", plotter.plot_data[0].attrs)

    def test_ideal_nonfixed(self):
        """Test the ideal formatoption"""
        self.test_nonfixed_fit()
        self.plotter.update(ideal=[self.default_intercept, self.default_slope])
        for i, da in enumerate(self.plotter.fit.iter_data):
            if da.ndim > 1:
                da = da[0]
            y = list(self.plotter.ax.lines[i * 2 + 1].get_ydata())
            ref = list(
                self.default_intercept
                + self.default_slope * da[da.dims[-1]].values
            )
            self.assertEqual(
                y, ref, msg="Array %i (%s) disagrees" % (i, da.psy.arr_name)
            )

    def test_ideal_fix0(self):
        """Test the ideal formatoption with fix point at 0"""
        self.test_fix0()
        self.plotter.update(ideal=[0, self.default_slope])
        for i, da in enumerate(self.plotter.fit.iter_data):
            if da.ndim > 1:
                da = da[0]
            y = list(self.plotter.ax.lines[i * 2 + 1].get_ydata())
            ref = list(self.default_slope * da[da.dims[-1]].values)
            self.assertEqual(
                y, ref, msg="Array %i (%s) disagrees" % (i, da.psy.arr_name)
            )

    def test_ideal_fix1(self):
        """Test the ideal formatoption with fix point at 1"""
        self.test_fix1()
        self.plotter.update(ideal=[1, self.default_slope])
        for i, da in enumerate(self.plotter.fit.iter_data):
            if da.ndim > 1:
                da = da[0]
            y = list(self.plotter.ax.lines[i * 2 + 1].get_ydata())
            ref = list(1 + self.default_slope * da[da.dims[-1]].values)
            self.assertEqual(
                y, ref, msg="Array %i (%s) disagrees" % (i, da.psy.arr_name)
            )

    def test_id_color(self):
        """Test the id_color formatoption"""
        self.test_ideal_nonfixed()
        ref_c = ["y"]
        self.plotter.update(id_color=ref_c)
        for i, da in enumerate(self.plotter.fit.iter_data):
            c = list(self.plotter.ax.lines[i * 2 + 1].get_color())
            self.assertEqual(
                c, ref_c, msg="Array %i (%s) disagrees" % (i, da.psy.arr_name)
            )

    def test_line_xlim(self):
        """Test the line_xlim formatoption"""
        self.test_ideal_nonfixed()
        data = self.plot_data
        coord = data[data.dims[1]]
        plot_fmt = self.fit_plot_fmt

        # test fixed limits
        self.plotter.update(line_xlim=(-5, 5))
        self.assertEqual(plot_fmt._plot[-1].get_xdata().min(), -5)
        self.assertEqual(plot_fmt._plot[-1].get_xdata().max(), 5)

        # test rounded limits
        self.plotter.update(line_xlim=("rounded", "rounded"))
        vmin, vmax = self.plotter.xrange._round_min_max(
            coord.min().values, coord.max().values
        )
        self.assertEqual(plot_fmt._plot[-1].get_xdata().min(), vmin)
        self.assertEqual(plot_fmt._plot[-1].get_xdata().max(), vmax)

    def test_line_xlim_2(self):
        """Test the line_xlim with two arrays"""
        sequence = self.define_data()
        sequence.append(sequence[0].copy(True), new_name=True)
        plotter = self.plotter_cls(sequence, line_xlim=[(0, 5), (5, 10)])
        self.assertEqual(plotter.plot_data[0].x.min().values, 0)
        self.assertEqual(plotter.plot_data[0].x.max().values, 5)
        self.assertEqual(plotter.plot_data[1].x.min().values, 5)
        self.assertEqual(plotter.plot_data[1].x.max().values, 10)


class SingleLinRegPlotterTest(LinRegPlotterTest):
    """Test the :class:`psyplot.plotter.linreg.LinRegPlotter` with a single
    data array not in a list"""

    @classmethod
    def define_data(cls, *args, **kwargs):
        return super(SingleLinRegPlotterTest, cls).define_data(
            *args, **kwargs
        )[0]

    @classmethod
    def define_curve_data(cls, *args, **kwargs):
        da, func = super(SingleLinRegPlotterTest, cls).define_curve_data(
            *args, **kwargs
        )
        return da[0], func

    @classmethod
    def define_poly_data(cls, *args, **kwargs):
        da, deg = super(SingleLinRegPlotterTest, cls).define_poly_data(
            *args, **kwargs
        )
        return da[0], deg

    @property
    def plot_data(self):
        return self.plotter.plot_data

    @unittest.skip("No need for two arrays")
    def test_line_xlim_2(self):
        pass

    @unittest.skip("No need for two arrays")
    def test_2fits(self):
        pass


class DensityRegPlotterTest(unittest.TestCase):
    """Test whether the plot works in combination with the
    :class:`psyplot.plotter.linreg.LinearRegressionPlotter`"""

    @classmethod
    def setUpClass(cls):
        cls.data = cls.define_data()
        cls.plotter = DensityRegPlotter(cls.data)

    @property
    def plot_data(self):
        return self.plotter.plot_data[0]

    @classmethod
    def define_data(cls, *args, **kwargs):
        return SingleLinRegPlotterTest.define_data(*args, **kwargs)

    @classmethod
    def tearDownClass(cls):
        import psyplot
        import psyplot.project as psy

        psyplot.rcParams.update_from_defaultParams()
        del cls.data
        psy.close("all")
        plt.close("all")

    def tearDown(self):
        self.plotter.update(todefault=True)

    @classmethod
    def update(cls, **kwargs):
        """Update the plotter of this test case"""
        cls.plotter.update(**kwargs)

    def test_bins(self):
        """Test the bins formatoption"""
        bins = [100, 10]
        self.update(bins=bins)
        self.assertEqual(len(self.plot_data.x), 100)
        self.assertEqual(len(self.plot_data.y), 10)

    def test_xrange(self):
        """Test the xrange formatoption"""
        data = self.data
        xrange = np.percentile(data.x.values, [25, 75])
        self.update(xrange=xrange)
        self.assertGreaterEqual(self.plot_data.x.min(), xrange[0])
        self.assertLessEqual(self.plot_data.x.max(), xrange[1])

        # now update to use the quantiles explicitely
        self.update(xrange=(["minmax", 25], ["minmax", 75]))
        self.assertGreaterEqual(self.plot_data.x.min(), xrange[0])
        self.assertLessEqual(self.plot_data.x.max(), xrange[1])

    def test_yrange(self):
        """Test the yrange formatoption"""
        data = self.data
        yrange = np.percentile(data.values, [25, 75])
        self.update(yrange=yrange)
        self.assertGreaterEqual(self.plot_data.y.min(), yrange[0])
        self.assertLessEqual(self.plot_data.y.max(), yrange[1])

        # now update to use the quantiles explicitely
        self.update(yrange=(["minmax", 25], ["minmax", 75]))
        self.assertGreaterEqual(self.plot_data.y.min(), yrange[0])
        self.assertLessEqual(self.plot_data.y.max(), yrange[1])

    def test_normed(self):
        """Test the normed formatoption"""
        self.update(normed="counts")
        data = self.plot_data
        self.assertAlmostEqual(data.values.sum(), 1.0)

        self.update(normed="area")
        data = self.plot_data
        a0, a1 = data.x.values[:2]
        b0, b1 = data.y.values[:2]
        area = (a1 - a0) * (b1 - b0)
        self.assertAlmostEqual((self.plot_data.values * area).sum(), 1.0)

    def test_coord(self):
        """Test whether we can use an alternative coordinate"""
        self.update(coord="v", xlabel="%(name)s")
        self.assertEqual(
            self.plotter.ax.get_xlabel(),
            "v",
            msg="Did not update to the right coordinate!",
        )


class DensityRegPlotterTestFits(SingleLinRegPlotterTest):
    """Test the fit part of the
    :class:`psyplot.plotter.linreg.DensityRegPlotter` class"""

    plotter_cls = DensityRegPlotter

    @property
    def plot_data(self):
        return self.plotter.plot_data[1]

    @property
    def fit_plot_fmt(self):
        return self.plotter.lineplot


if __name__ == "__main__":
    unittest.main()
