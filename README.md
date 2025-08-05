def f(x, y):
    return 3 * x**2 * y + 2 * y**3

# Analytical derivatives
def df_dx(x, y):
    return 6 * x * y

def df_dy(x, y):
    return 3 * x**2 + 6 * y**2

# Numerical derivatives using finite differences
def numerical_partial_derivatives(f, x, y, h=1e-5):
    dfdx = (f(x + h, y) - f(x, y)) / h
    dfdy = (f(x, y + h) - f(x, y)) / h
    return dfdx, dfdy

if __name__ == "__main__":
    x = 1
    y = 2

    print("Analytical partial derivatives at (x=1, y=2):")
    print("∂f/∂x =", df_dx(x, y))
    print("∂f/∂y =", df_dy(x, y))

    dfdx_num, dfdy_num = numerical_partial_derivatives(f, x, y)
    print("\nNumerical partial derivatives at (x=1, y=2):")
    print("∂f/∂x ≈", dfdx_num)
    print("∂f/∂y ≈", dfdy_num)