# mobile_price_prediction as api

data used- https://www.kaggle.com/iabhishekofficial/mobile-price-classification
# Features

   - battery_power (Measured in mAh)
   - dual_sim (Has Dual sim support or not)
   - fc (front camera in MegaPixels)
   - pc (primary camera in MegaPixels)
   - int_memory (Internal Memory in Gigabytes)
   - n_cores (Number of cores of processor)
   - ram (Random Access Memory in MegaBytes)

# Label

   - predicted cost (0(low cost), 1(medium cost), 2(high cost) and 3(very high cost))

# to run api app

   - first go into folder where your api.py saved
   - run this in terminal **uvicorn api:api_app --port <your_port_number> --reload**

