import pytest
from my_project import calculate_number_of_pieces, calculate_required_bars, calculate_total_time

def test_calculate_number_of_pieces():
    bar_length = 6000
    part_size = 100.0
    
    pieces_per_bar = calculate_number_of_pieces(bar_length, part_size)

    assert pieces_per_bar == 60.0
    assert isinstance(pieces_per_bar, float)

def test_calculate_required_bars():
    pieces_needed = 250
    pieces_per_bar = 60.0

    required_bars = calculate_required_bars(pieces_needed, pieces_per_bar)
    
    assert required_bars == 5
    assert isinstance(required_bars, int)

def test_calculate_total_time():
    required_bars = 5
    time_per_bar_minutes = 10.5

    total_time = calculate_total_time(required_bars, time_per_bar_minutes)
    
    assert total_time == 52.5
    assert isinstance(total_time, float)

if __name__ == '__main__':
    pytest.main(["-v", "--tb=line", "-rN", __file__])
