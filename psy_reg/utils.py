"""Utility functions for psy-reg"""
import abc
import inspect
from itertools import cycle
from scipy.optimize import curve_fit, differential_evolution
import numpy as np
from warnings import warn


def rsquared(sim, obs):
    r"""Calculate the R-squared (coefficient of determination, $R^2$)

    $R^2$ is defined as

    .. math::

        R^2 = 1 - \frac{\sum\,(obs - sim)^2}{\sum(obs - \widebar{obs})^2}

    Parameters
    ----------
    sim: np.ndarray
        Simulated values
    obs: np.ndarray
        Observed values (broadcastable to `sim`)

    Returns
    -------
    float
        The R squared"""
    residuals = obs - sim
    ss_res = (residuals ** 2).sum()
    ss_tot = ((obs - obs.mean()) ** 2).sum()
    return 1 - (ss_res / ss_tot)


class GenericModel(metaclass=abc.ABCMeta):
    """An abstract model for least-squares regression

    This abstract base class implements a fit and predict and can be subclassed
    to provide a model for a function that is fitted with the
    :func:`scipy.optimize.curve_fit` function."""

    def __init__(self, *params, **attrs):
        self.params = params
        self.attrs = attrs

        kws = self.func_kwargs
        if kws is not None:
            self.attrs.update(kws)

    @property
    def rsquared(self):
        """The coefficient of determination, $R^2$"""
        return self.attrs.get('rsquared', None)

    @property
    def pcov(self):
        """The covariance matrix"""
        return self.attrs.get('pcov', None)

    @property
    def func_kwargs(self):
        """The arguments for the fit function if the :attr:`method` is
        'curve_fit'"""
        argspec = inspect.getfullargspec(self.function)
        args = argspec.args[1:]
        if len(args) < len(self.params):
            return None
        else:
            return dict(zip(args, self.params))

    @classmethod
    def func_args(cls):
        """The arguments for the fit function if the :attr:`method` is
        'curve_fit'"""
        argspec = inspect.getfullargspec(cls.function)
        return argspec.args[1:]

    @classmethod
    def estimate_p0(cls, x, y, bounds):
        def objective(params):
            # the sum of squared errors
            return np.sum((y - cls.function(x, *params)) ** 2)

        if bounds is None or np.isinf(bounds).any():
            warn("Need finite parameter boundaries for automatic initial "
                 "parameter estimation!",
                 RuntimeWarning)
            return None
        if np.ndim(bounds) == 1:
            bounds = [bounds]
        args = cls.func_args()
        bounds = [t for t, arg in zip(cycle(bounds), args)]

        result = differential_evolution(objective, bounds)
        if result.success:
            return result.x
        else:  # return default values
            warn('Could not estimate initial parameters! Reason: %s' % (
                result.message, ), RuntimeWarning)
            return None

    @staticmethod
    @abc.abstractmethod
    def function(x, *params, **kwargs):
        """The function that is responsible for the fit"""

    def __call__(self, x):
        return self.predict(x)

    def predict(self, x):
        return self.function(x, *self.params)

    @classmethod
    def fit(cls, x, y, *args, **kwargs):
        params, pcov = curve_fit(cls.function, x, y, *args, **kwargs)
        predicted = cls.function(x, *params)
        attrs = dict(rsquared=rsquared(predicted, y),
                     pcov=pcov)
        if pcov.size == 1:
            attrs['err'] = np.sqrt(pcov)[0, 0]

        return cls(*params, **attrs)
