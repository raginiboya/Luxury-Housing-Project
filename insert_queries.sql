-- Sample insert structure used for loading cleaned data

INSERT INTO housing_data (
    Property_ID,
    Developer_Name,
    Project_Name,
    Micro_Market,
    Configuration,
    Unit_Size_Sqft,
    Ticket_Price_Cr,
    Sales_Channel,
    Buyer_Type,
    Possession_Status,
    Booking_Count,
    Purchase_Quarter,
    Quarter_Number,
    Amenity_Score,
    Connectivity_Score,
    Locality_Infra_Score,
    Avg_Traffic_Time,
    NRI_Buyer,
    Transaction_Type
)
VALUES
(
    1,
    'Prestige',
    'Project_1',
    'Whitefield',
    '3BHK',
    1650,
    2.75,
    'Online',
    'End User',
    'Ready To Move',
    1,
    'Q1',
    1,
    8.5,
    7.8,
    8.2,
    35,
    'No',
    'Primary'
);