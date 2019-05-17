# Copyright 2019 Streamlit Inc. All rights reserved.

"""Tests coercing various objects to DataFrames"""

# Python 2/3 compatibility
from __future__ import print_function, division, unicode_literals, absolute_import
from streamlit.compatibility import setup_2_3_shims

from streamlit.elements.data_frame_proto import convert_anything_to_df

setup_2_3_shims(globals())

import unittest
import pandas as pd
import numpy as np


class DataFrameCoercionTest(unittest.TestCase):
    def test_dict_of_lists(self):
        """Test that a DataFrame can be constructed from a dict
        of equal-length lists
        """
        d = {'a': [1], 'b': [2], 'c': [3]}
        df = convert_anything_to_df(d)
        self.assertEqual(type(df), pd.DataFrame)
        self.assertEqual(df.shape, (1, 3))

    def test_empty_numpy_array(self):
        """Test that a single-column empty DataFrame can be constructed
        from an empty numpy array.
        """
        arr = np.array([])
        df = convert_anything_to_df(arr)
        self.assertEqual(type(df), pd.DataFrame)
        self.assertEqual(df.shape, (0, 1))

    def test_styler(self):
        """Test that a DataFrame can be constructed from a pandas.Styler"""
        d = {'a': [1], 'b': [2], 'c': [3]}
        styler = pd.DataFrame(d).style.format('{:.2%}')
        df = convert_anything_to_df(styler)
        self.assertEqual(type(df), pd.DataFrame)
        self.assertEqual(df.shape, (1, 3))
