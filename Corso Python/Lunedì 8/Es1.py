import numpy as np


arr = np.arange(10,50)


print(f"Il formato iniziale: {arr.dtype}")
      

arr = arr.astype(np.float64)

print(f"Il formato iniziale: {arr.dtype}")


print(arr.dtype)


print(f"La forma dell'array è la seguente:\n{arr}")