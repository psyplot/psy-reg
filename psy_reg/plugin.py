"""psy-simple psyplot plugin

This module defines the rcParams for the psy-simple plugin"""
import six
from numpy import asarray
from psyplot.config.rcsetup import RcParams
from psy_simple.plugin import (
    try_and_error, validate_float, validate_none, validate_limits,
    validate_dict, validate_int, validate_cmap, validate_str,
    ValidateList,
    ValidateInStrings, safe_list, rcParams as psyps_rc)
from psyplot.compat.pycompat import map, filter
from psy_reg import __version__ as plugin_version


def get_versions(requirements=True):
    if requirements:
        import scipy
        import statsmodels
        return {'version': plugin_version,
                'requirements': {'scipy': scipy.__version__,
                                 'statsmodels': statsmodels.__version__}}
    else:
        return {'version': plugin_version}


def patch_prior_1_0(plotter_d, versions):
    """Patch psy_reg plotters for versions smaller than 1.0

    Before psyplot 1.0.0, the plotters in the psy_reg package where part of the
    psyplot.plotter.linreg module. This has to be corrected"""
    plotter_d['cls'] = ('psy_reg.plotters', plotter_d['cls'][1])


#: patches to apply when loading a project
patches = {
    ('psyplot.plotter.linreg', 'LinRegPlotter'): patch_prior_1_0,
    ('psyplot.plotter.linreg', 'DensityRegPlotter'): patch_prior_1_0,
    }


# -----------------------------------------------------------------------------
# ------------------------- validation functions ------------------------------
# -----------------------------------------------------------------------------


def validate_iter(value):
    """Validate that the given value is an iterable"""
    try:
        return iter(value)
    except TypeError:
        raise ValueError("%s is not an iterable!" % repr(value))


def validate_callable(val):
    if callable(val):
        return val
    raise ValueError('%s is not callable!' % str(val))


def validate_fit(val):
    def validate(val):
        if isinstance(val, six.string_types) and val.startswith('poly'):
            try:
                int(val[4:])
            except ValueError:
                raise ValueError("Polynomials must be of the form 'poly<deg>' "
                                 "(e.g. 'poly3'), not %s!" % val)
            else:
                return val
        elif hasattr(val, 'fit') and hasattr(val, 'predict'):
            return val
        return try_and_error(
            validate_callable, validate_none,
            ValidateInStrings('fit', ['fit', 'linear', 'robust'], True))(val)
    return list(map(validate, safe_list(val)))


class validate_list(object):
    """Validate a list of the specified `dtype`

    Parameters
    ----------
    dtype: object
        A datatype (e.g. :class:`float`) that shall be used for the conversion
    """

    def __init__(self, dtype=None, length=None, listtype=list):
        """Initialization function"""
        #: data type (e.g. :class:`float`) used for the conversion
        self.dtype = dtype
        self.length = length
        self.listtype = list

    def __call__(self, l):
        """Validate whether `l` is a list with contents of :attr:`dtype`

        Parameters
        ----------
        l: list-like

        Returns
        -------
        list
            list with values of dtype :attr:`dtype`

        Raises
        ------
        ValueError"""
        try:
            if self.dtype is None:
                l = self.listtype(l)
            else:
                l = self.listtype(map(self.dtype, l))
        except TypeError:
            if self.dtype is None:
                raise ValueError(
                    "Could not convert to list!")
            else:
                raise ValueError(
                    "Could not convert to list of type %s!" % str(self.dtype))
        if self.length is not None and len(l) != self.length:
            raise ValueError('List with length %i is required! Not %i!' % (
                self.length, len(l)))
        return l


def validate_stringlist(s):
    """Validate a list of strings

    Parameters
    ----------
    val: iterable of strings

    Returns
    -------
    list
        list of str

    Raises
    ------
    ValueError"""
    if isinstance(s, six.string_types):
        return [six.text_type(v.strip()) for v in s.split(',') if v.strip()]
    else:
        try:
            return [six.text_type(v) for v in s if v]
        except TypeError as e:
            raise ValueError(e.message)


def validate_fix(val):
    if val is None:
        return [None]
    try:
        val = validate_float(val)
        return [[0, val]]
    except ValueError:
        pass
    msg = 'Values for the fix formatoptions must be of length 2!'
    validator = try_and_error(validate_none, validate_list(float))
    try:
        val = validator(val)
    except ValueError:
        val = list(map(validator, val))
        if not all(v is None or len(v) == 2 for v in val):
            raise ValueError(msg)
    else:
        if val is not None and len(val) != 2:
            raise ValueError(msg)
    return val


def validate_ideal(val):
    try:
        return validate_none(val)
    except ValueError:
        val = asarray(val).astype(float)
        if val.ndim == 1:
            return val.reshape(1, val.size).tolist()
        elif val.ndim == 2:
            return val.tolist()
        raise ValueError(
            "Only 1- and 2-dimensional arrays are allowed! Got %s" % (val, ))


def validate_param_bounds(value):
    if value is None:
        return [None]
    else:
        f = value[0]
        try:
            f = next(filter(lambda v: v is not None, validate_iter(value)))
        except StopIteration:
            return value
        else:
            try:
                f[0]
            except TypeError:  # found only one tuple
                return [value]
            else:
                return value


def validate_p0(value):
    value = safe_list(value)
    for i, v in enumerate(value):
        value[i] = try_and_error(ValidateList(float),
                                 ValidateInStrings('p0', ['auto'], True))(v)
    return value


def validate_line_xlim(val):
    if isinstance(val, six.string_types):
        val = (val, val)
    val = asarray(safe_list(val))
    if val.ndim == 1:
        val = asarray([val])
    return list(map(validate_limits, val.tolist()))


# -----------------------------------------------------------------------------
# ------------------------------ rcParams -------------------------------------
# -----------------------------------------------------------------------------


#: the :class:`~psyplot.config.rcsetup.RcParams` for the psy-reg plugin
rcParams = RcParams(defaultParams={

    # -------------------------------------------------------------------------
    # ----------------------- Registered plotters -----------------------------
    # -------------------------------------------------------------------------

    'project.plotters': [

        {'linreg': {
             'module': 'psy_reg.plotters',
             'plotter_name': 'LinRegPlotter',
             'prefer_list': True,
             'default_slice': None,
             'summary': 'Draw a fit from x to y'},
         'densityreg': {
             'module': 'psy_reg.plotters',
             'plotter_name': 'DensityRegPlotter',
             'prefer_list': False,
             'default_slice': None,
             'summary': ('Make a density plot and draw a fit from x to y of '
                         'points')},
         }, validate_dict],

    # -------------------------------------------------------------------------
    # --------------------- Default formatoptions -----------------------------
    # -------------------------------------------------------------------------
    # Linear regression
    'plotter.linreg.xrange': [
        'minmax', validate_limits, 'The fit limits of the line plot'],
    'plotter.linreg.yrange': [
        'minmax', validate_limits, 'The fit limits of the line plot'],
    'plotter.linreg.line_xlim': [
        'minmax', validate_line_xlim,
        'The x-limits of the drawn best fit line'],
    'plotter.linreg.param_bounds': [
        None, validate_param_bounds,
        'fmt key to specify the boundaries of the fit'],
    'plotter.linreg.p0': [
        'auto', validate_p0,
        'fmt key to specify the initial parameters of the fit'],
    'plotter.linreg.fix': [
        None, validate_fix,
        'fmt key to set a fix point for the linear regression fit'],
    'plotter.linreg.fit': [
        'fit', validate_fit, 'The model to use for fitting a model'],
    'plotter.linreg.nboot': [
        1000, validate_int,
        'Number of bootstrap resamples to estimate the confidence interval'],
    'plotter.linreg.ci': [
        95, try_and_error(validate_none, validate_float),
        'Size of the confidence interval'],
    'plotter.linreg.id_color': [
        None, psyps_rc.validate['plotter.simple.color'],
        'fmt key to modify the color cycle of the ideal lines in a fit plot'],
    'plotter.linreg.ideal': [
        None, validate_ideal,
        'The ideal lines to plot'],
    'plotter.linreg.bootstrap.random_seed': [
        None, try_and_error(validate_none, validate_int),
        'The seed to use for the bootstrap algorithm to estimate the '
        'confidence interval'],

    # combined density and linear regression plot
    'plotter.densityreg.lineplot': [
        '-', try_and_error(validate_none, validate_str,
                           validate_stringlist),
        'fmt key to modify the line style'],
    })

rcParams.update_from_defaultParams()
