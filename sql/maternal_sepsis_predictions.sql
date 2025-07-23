CREATE DATABASE MaternalSepsisDB;

USE MaternalSepsisDB;

-- Drop the existing table
DROP TABLE IF EXISTS maternal_sepsis_dataset;

-- Recreate the table
CREATE TABLE maternal_sepsis_dataset (
    Patient_ID VARCHAR(36),
    Age INT,
    Parity INT,
    BMI FLOAT,
    Pre_existing_conditions VARCHAR(50),
    C_section_type VARCHAR(50),
    Duration_surgery_min INT,
    Blood_loss_ml INT,
    Antibiotics_given VARCHAR(10),
    Indication_for_C_section VARCHAR(50),
    Temperature_C FLOAT,
    Heart_rate_bpm INT,
    Respiratory_rate_bpm INT,
    BP_systolic_mmHg INT,
    BP_diastolic_mmHg INT,
    SpO2_percent FLOAT,
    WBC_count_x10_9_L FLOAT,
    CRP_mg_L FLOAT,
    Procalcitonin_ng_mL FLOAT,
    Lactate_mmol_L FLOAT,
    Blood_culture_result VARCHAR(50),
    Wound_status VARCHAR(50),
    Uterine_tenderness VARCHAR(10),
    Urine_output_ml_hr INT,
    Organ_dysfunction VARCHAR(10),
    Sepsis_detected VARCHAR(10),
    Time_to_diagnosis_hr FLOAT,
    Outcome VARCHAR(50)
);


-- Step 2: Import the CSV using BULK INSERT with corrected file path
BULK INSERT maternal_sepsis_dataset
FROM 'C:\\Users\\Titan\\Documents\\maternal_sepsis_dataset.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    FORMAT = 'CSV',
    FIELDQUOTE = '"',
    DATAFILETYPE = 'char',
    TABLOCK
);

-- Step 3: Clean negative CRP values
UPDATE maternal_sepsis_dataset
SET CRP_mg_L = 0
WHERE CRP_mg_L < 0;


-- Step 4: Apply sepsis prediction logic and store results
SELECT 
    Patient_ID,
    Temperature_C,
    WBC_count_x10_9_L,
    CRP_mg_L,
    Organ_dysfunction,
    CASE 
        WHEN (Temperature_C > 38.5 AND WBC_count_x10_9_L > 12 AND CRP_mg_L > 50) 
             OR Organ_dysfunction = 'Yes' 
        THEN 'Yes' 
        ELSE 'No' 
    END AS Sepsis_detected,
    CASE 
        WHEN (Temperature_C > 38.5 AND WBC_count_x10_9_L > 12 AND CRP_mg_L > 50) 
             OR Organ_dysfunction = 'Yes' 
        THEN FLOOR(1 + (RAND(CHECKSUM(NEWID())) * 48)) 
        ELSE NULL 
    END AS Time_to_diagnosis_hr,
    CASE 
        WHEN (Temperature_C > 38.5 AND WBC_count_x10_9_L > 12 AND CRP_mg_L > 50) 
             OR Organ_dysfunction = 'Yes' 
        THEN CASE FLOOR(1 + (RAND(CHECKSUM(NEWID())) * 3))
                WHEN 1 THEN 'Recovered'
                WHEN 2 THEN 'ICU'
                WHEN 3 THEN 'Mortality'
             END
        ELSE 'Recovered'
    END AS Outcome
INTO maternal_sepsis_predictions
FROM maternal_sepsis_dataset;


-- Step 5: View the results
SELECT TOP 5 
    Patient_ID,
    Temperature_C,
    WBC_count_x10_9_L,
    CRP_mg_L,
    Organ_dysfunction,
    Sepsis_detected,
    Time_to_diagnosis_hr,
    Outcome
FROM maternal_sepsis_predictions;