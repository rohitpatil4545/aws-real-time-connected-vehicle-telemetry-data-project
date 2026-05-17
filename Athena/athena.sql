CREATE DATABASE vehicle_telemetry;  

CREATE EXTERNAL TABLE vehicle_data (
    vehicle_id string,
    speed int,
    engine_temp int,
    fuel_level int,
    timestamp string
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://vehicle-telemetry-dataproject/telemetry/'; 

select * from vehicle_data ;