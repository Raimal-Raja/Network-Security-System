import os
import tempfile
import unittest

import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

from networksecurity.utils.main_utils.utils import (
    evaluate_models, load_object, save_object, write_yaml_file,
    save_numpy_array_data, load_numpy_array_data,
)


class ModelSelectionTests(unittest.TestCase):
    def test_macro_f1_uses_training_folds_and_keeps_test_data_untouched(self):
        x = np.arange(30).reshape(-1, 1)
        y = np.array([0] * 15 + [1] * 15)
        models = {'tree': DecisionTreeClassifier(random_state=0),
                  'dummy': DummyClassifier(strategy='most_frequent')}
        expected = cross_val_score(models['tree'], x, y, cv=3, scoring='f1_macro').mean()
        # Deliberately unusable holdout: selection must never predict on it.
        scores = evaluate_models(x, y, object(), object(), models,
                                 {'tree': {}, 'dummy': {}})
        self.assertAlmostEqual(scores['tree'], expected)
        self.assertGreater(scores['tree'], scores['dummy'])
        self.assertEqual(len(models['tree'].predict(x)), len(y))

    def test_artifact_helpers_accept_names_in_current_directory(self):
        previous = os.getcwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                save_object('model.pkl', {'ok': True})
                self.assertEqual(load_object('model.pkl'), {'ok': True})
                write_yaml_file('config.yaml', {'ok': True})
                save_numpy_array_data('array.npy', np.array([1, 2]))
                np.testing.assert_array_equal(load_numpy_array_data('array.npy'), [1, 2])
            finally:
                os.chdir(previous)


if __name__ == '__main__':
    unittest.main()
