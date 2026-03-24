-- 1. Count total records
SELECT COUNT(*) AS Total_Records
FROM housing_data;

-- 2. Group by Booking Status
SELECT Possession_Status,
       COUNT(*) AS Booking_Count
FROM housing_data
GROUP BY Possession_Status;

-- 3. Average Ticket Price per Builder
SELECT Developer_Name,
       AVG(Ticket_Price_Cr) AS Avg_Ticket_Price
FROM housing_data
GROUP BY Developer_Name;