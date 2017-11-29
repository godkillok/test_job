# coding: utf-8

import csv
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests

# with open('/home/tom/Desktop/book1.csv','r') as f:
#     reader = csv.reader(f)
#     result=[]
#
#     for row in reader:
#         result.append(row)
# result.pop(0)
# r_1=[]
# for l in result:
#     r=[]
#     for i in l:
#         r.append(float(i))
#     r_1.append(r)
#
# result_np=np.array(r_1)
# result_np=result_np[:,1:]
# print(result_np)
#
#
# # input=np.diff(input, axis=0)
# # input=np.random.rand(100,2)
# final_result=[]
# for i in range(8):
#     for j in range(8):
#         input = result_np[:, i]
#         input = np.c_[input, result_np[:, j]]
#         reg=grangercausalitytests(input,3)
#         if reg[3][0]['params_ftest'][1]<0.05:
#             a=True
#         else:
#             a=False
#         final_result.append([i,j,a])
#
#
# print(final_result)

#
from statsmodels.compat.python import lrange
from statsmodels.tsa.stattools import (adfuller, acf, pacf_ols, pacf_yw,
                                       pacf, grangercausalitytests,
                                       coint, acovf, kpss, ResultsStore,
                                       arma_order_select_ic)
from statsmodels.tsa.base.datetools import dates_from_range
import numpy as np
from numpy.testing import (assert_almost_equal, assert_equal, assert_warns,
                           assert_raises, dec, assert_, assert_allclose)
from numpy import genfromtxt
from statsmodels.datasets import macrodata, sunspots
from pandas import Series, Index, DataFrame
import os
import warnings
from statsmodels.tools.sm_exceptions import MissingDataError

DECIMAL_8 = 8
DECIMAL_6 = 6
DECIMAL_5 = 5
DECIMAL_4 = 4
DECIMAL_3 = 3
DECIMAL_2 = 2
DECIMAL_1 = 1



class TestGrangerCausality(object):
    def test_grangercausality(self):
        # some example data
        mdata = macrodata.load().data
        mdata = mdata[['realgdp', 'realcons']]
        data = mdata.view((float, 2))
        data = np.diff(np.log(data), axis=0)
        print(data)
        # R: lmtest:grangertest
        r_result = [0.243097, 0.7844328, 195, 2]  # f_test
        gr = grangercausalitytests(data[:, 1::-1], 2, verbose=True)
        # assert_almost_equal(r_result, gr[2][0]['ssr_ftest'], decimal=7)
        # assert_almost_equal(gr[2][0]['params_ftest'], gr[2][0]['ssr_ftest'], decimal=7)

    def test_granger_fails_on_nobs_check(self):
        # Test that if maxlag is too large, Granger Test raises a clear error.
        X = np.random.rand(10, 1)
        x = np.c_[X, X[:,0]+2]
        X=np.c_[X, X[:,0]*2]


        grangercausalitytests(X, 2, verbose=True)  # This should pass.
        grangercausalitytests(x, 2, verbose=True)
        assert_raises(ValueError, grangercausalitytests, X, 3, verbose=False)


if __name__ == "__main__":
    import nose
    #    nose.runmodule(argv=[__file__, '-vvs','-x','-pdb'], exit=False)
    import numpy as np

    tg=TestGrangerCausality()
    tg.test_grangercausality()
    # np.testing.run_module_suite()