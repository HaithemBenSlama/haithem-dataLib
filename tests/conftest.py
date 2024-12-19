import pytest
import matplotlib
import matplotlib.pyplot as plt

# Set matplotlib to use a non-GUI backend
matplotlib.use('Agg')

@pytest.fixture(autouse=True)
def close_plots_after_test():
    """Automatically close any plots after each test."""
    yield  # Let the test run
    plt.close('all')  # Close all plots after the test finishes
