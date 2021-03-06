from unittest.mock import patch
from dataclasses import dataclass

import pytest

from mashumaro.meta.helpers import is_generic, is_class_var, is_init_var
from mashumaro import DataClassDictMixin


def test_is_generic_unsupported_python():
    with patch('mashumaro.meta.helpers.PY_36', False):
        with patch('mashumaro.meta.helpers.PY_37', False):
            with patch('mashumaro.meta.helpers.PY_38', False):
                with pytest.raises(NotImplementedError):
                    is_generic(int)


def test_is_class_var_unsupported_python():
    with patch('mashumaro.meta.helpers.PY_36', False):
        with patch('mashumaro.meta.helpers.PY_37', False):
            with patch('mashumaro.meta.helpers.PY_38', False):
                with pytest.raises(NotImplementedError):
                    is_class_var(int)


def test_is_init_var_unsupported_python():
    with patch('mashumaro.meta.helpers.PY_36', False):
        with patch('mashumaro.meta.helpers.PY_37', False):
            with patch('mashumaro.meta.helpers.PY_38', False):
                with pytest.raises(NotImplementedError):
                    is_init_var(int)


def test_no_code_builder():
    with patch('mashumaro.serializer.base.dict.'
               'DataClassDictMixin.__init_subclass__', lambda: ...):
        @dataclass
        class DataClass(DataClassDictMixin):
            pass
        assert DataClass.from_dict({}) is None
        assert DataClass().to_dict() is None
