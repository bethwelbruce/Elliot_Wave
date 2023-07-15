import numpy as np

def elliott_oscillator(data, fast_period=5, slow_period=34):
  """
  Calculates the Elliott oscillator indicator.

  Args:
    data: The price data.
    fast_period: The number of periods for the fast moving average.
    slow_period: The number of periods for the slow moving average.

  Returns:
    The Elliott oscillator indicator.
  """

  fast_sma = np.mean(data[-fast_period:], axis=0)
  slow_sma = np.mean(data[-slow_period:], axis=0)
  oscillator = fast_sma - slow_sma
  return oscillator

def main():
  """
  Main function.
  """

  data = np.random.randint(100, 200, (100, 1))
  oscillator = elliott_oscillator(data, fast_period=5, slow_period=34)
  print(oscillator)

if __name__ == "__main__":
  main()
