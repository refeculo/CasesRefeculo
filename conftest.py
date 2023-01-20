import pytest

# Относится к каждому методу
@pytest.fixture()
def set_up():
    print("\nНачало теста")
    yield
    print("\nКонец теста")

# Относится ко всем методам методу, но нужно чтобы хотяб в одном был
@pytest.fixture(scope="module")
def set_group():
    print("\nВход в систему")
    yield
    print("\nВыход из системы")