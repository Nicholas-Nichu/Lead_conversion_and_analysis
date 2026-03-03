--Using SQL to join tables and create a master table
DROP TABLE IF EXISTS "NPX1";

--Create a dummy table and join all the data from different tables with Lead ID as the primary key
CREATE TABLE "NPX1" AS SELECT * FROM
(
SELECT LSR."Lead", LSR."Created Date", LSR."Customer Name", LSR."User", LSR."Status",LSR."Channel",LSR."Sub Channel",
LSR."Last Note",SV."Site-Visit Done Date",SV."Site Visit Count",SV."Priority",DR."Reason",
CV."Key_Flat_Number",CV."Applicant DOB",CV."Applicant Occupation",CV."Name of the Organisation",CV."Booking Date:" as "Booking Date"
FROM "LSR_V2" AS LSR
LEFT JOIN "SV_V2" AS SV
ON LSR."Lead" = SV."Lead Id"
LEFT JOIN "DISQ_REASON" AS DR
ON LSR."Lead"=DR."Lead Id"
LEFT JOIN "CV" AS CV
on LSR."Lead"=CV."Lead ID"
);

--Create a table and select unique values of Lead ID from the dummy table to make sure only unique values get captured
DROP TABLE IF EXISTS "PX1";

CREATE TABLE "PX1" AS SELECT * FROM(
SELECT DISTINCT ON ("Lead") *
FROM "NPX1"
ORDER BY "Lead", "Booking Date" DESC NULLS LAST, "Site-Visit Done Date" ASC);
