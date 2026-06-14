USe oladb;

-- SQL Questions-----

-- 1. Retrieve all successful bookings:
SELECT * 
FROM olarides 
WHERE Booking_Status = 'Success';

-- 2. Find the average ride distance for each vehicle type:
SELECT Vehicle_Type,AVG(Ride_Distance) 
FROM olarides 
GROUP BY Vehicle_Type ;

-- 3. Get the total number of cancelled rides by customers:
SELECT COUNT(*) AS Rides_Cancelled_By_Customer 
FROM olarides 
WHERE Booking_Status = 'Canceled by Customer';

-- 4. List the top 5 customers who booked the highest number of rides:
SELECT Customer_ID, COUNT(*) AS Highest_NUMBER_OF_RIDES 
FROM olarides 
GROUP BY Customer_ID 
ORDER BY Highest_NUMBER_OF_RIDES DESC LIMIT 5;

-- 5. Get the number of rides cancelled by drivers due to personal and car-related issues:
SELECT Booking_Status,Canceled_Rides_by_Driver,COUNT(*) AS Rides_Cancelled 
FROM olarides 
WHERE Booking_Status = 'Canceled by Driver' and Canceled_Rides_by_Driver = 'Personal & Car related issue';

-- 6. Find the maximum and minimum driver ratings for Prime Sedan bookings:
SELECT Vehicle_Type, MAX(Driver_Ratings) AS MAX_Rating, MIN(Driver_Ratings) AS MIN_Rating 
FROM olarides 
WHERE Vehicle_Type = 'Prime Sedan';

-- 7. Retrieve all rides where payment was made using UPI:
SELECT * 
FROM olarides 
WHERE Payment_Method = 'UPI';

-- 8. Find the average customer rating per vehicle type:
SELECT Vehicle_Type,AVG(Customer_Rating) AS AVG_Customer_Rating 
FROM olarides 
GROUP BY Vehicle_Type;

-- 9. Calculate the total booking value of rides completed successfully:
SELECT Booking_Status,SUM(Booking_Value) AS Total_Booking_Value 
FROM olarides 
WHERE Booking_Status = 'success';

-- 10. List all incomplete rides along with the reason
SELECT 'Date',Booking_ID,Booking_Status,Customer_ID,Vehicle_Type,Incomplete_Rides,Incomplete_Rides_Reason 
FROM olarides 
WHERE Incomplete_Rides='Yes';
