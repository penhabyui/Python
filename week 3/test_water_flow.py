from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, \
    pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
from pytest import approx
import pytest

def test_water_colum_height():
    s = water_column_height(0.0,0.0)
    assert s == approx (0.0)

    s = water_column_height(0.0,10.0)
    assert s == approx (7.5)

    s = water_column_height(25.0,0.0)
    assert s == approx (25.0)
    
    s = water_column_height(48.3,12.8)
    assert s == approx (57.9)

def test_pressure_gain_from_water_height():
    a = pressure_gain_from_water_height(0.0)
    assert a == approx(0.000, abs= 0.001)

    a = pressure_gain_from_water_height(30.2)
    assert a == approx(295.628, abs= 0.001)

    a = pressure_gain_from_water_height(50.0)
    assert a == approx(489.450, abs= 0.001)

def test_pressure_loss_from_pipe():
    p = pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75)
    assert p == approx(0.000, abs = 0.001)

    p = pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75)
    assert p == approx(0.000, abs = 0.001)

    p = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00)
    assert p == approx(0.000, abs = 0.001)

    p = pressure_loss_from_pipe( 0.048692, 200.00, 0.018, 1.75)
    assert p == approx(-113.008, abs = 0.001)

    p = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65)
    assert p == approx(-100.462, abs = 0.001)

    p = pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65)
    assert p == approx(-61.576, abs = 0.001)

    p = pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65)
    assert p == approx(-110.884, abs = 0.001)

def test_pressure_loss_from_fittings():
    pf = pressure_loss_from_fittings(0.00, 3) 
    assert pf == approx(0.000, abs = 0.001) 

    pf = pressure_loss_from_fittings(1.65, 0) 
    assert pf == approx(0.000, abs = 0.001)

    pf = pressure_loss_from_fittings(1.65, 2) 
    assert pf == approx(-0.109, abs = 0.001)

    pf = pressure_loss_from_fittings(1.75, 2) 
    assert pf == approx(-0.122, abs = 0.001)

    pf = pressure_loss_from_fittings(1.75, 5) 
    assert pf == approx(-0.306, abs = 0.001)

def test_reynolds_number():
    rn = reynolds_number(0.048692, 0.00)
    assert rn == approx(0, abs = 1)

    rn = reynolds_number(0.048692, 1.65)
    assert rn == approx(80069, abs = 1)

    rn = reynolds_number(0.048692, 1.75)
    assert rn == approx(84922, abs = 1)

    rn = reynolds_number(0.286870, 1.65)
    assert rn == approx(471729, abs = 1)

    rn = reynolds_number(0.286870, 1.75)
    assert rn == approx(500318, abs = 1)

def test_pressure_loss_from_pipe_reduction():
    ppr = pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692)
    assert ppr == approx(0.000, abs = 0.001)

    ppr = pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert ppr == approx(-163.744, abs = 0.001)

    ppr = pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert ppr == approx(-184.182, abs = 0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])    