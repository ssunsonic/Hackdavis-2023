# Hackdavis Project

Problem Statement: The Aggie Reuse Store currently has no way of monitoring the store's foot traffic, so they do not know how many students come in every week, when the students tend to come in, and what days of the week are most popular. Operating hours change from quarter to quarter, so they want to use customer traffic data to know when the most optimal time to open is and how to better staff their volunteers to support rush hour.

- Forecasting/Predictions
- Hardware: Arduino wired to a ultrasonic sensor -> imitate motion sensor
- Front-End: Built with React.js, Charts.js plugin to create graphs. Read json files, in order to map out data.
- Visualization

File Description:
- forecast.py: Python file that forecast based on the data from Day_m.csv model, built with LSTM Neural Network technique and python.
- Day_m.csv: Data mapped from monthly_milk_production.csv containing columns of Day and Footprint of that Day in the week.
- monthly_milk_production.csv: Cyclic Data that present a seasonal trend; used to mimik the footprints of the Used Store

Website:
- Run `by cd my-app`, and `npm start`
- Graphs created with Chart.js are slighlty interactive with hover effect.
- Nice color theme, with a simple straight forward landing page designed to deliver information promptly.
- Drop down menu for smaller screens, but unutilized.

Link to Demo:
https://youtu.be/5ulnhIoJCjE

Link to HackDavis Submission:
https://devpost.com/software/happy-feet
