"""Constants for the sunpower integration."""
from homeassistant.const import (
    TIME_SECONDS,
    DATA_KILOBYTES,
    FREQUENCY_HERTZ,
    ENERGY_KILO_WATT_HOUR,
    POWER_KILO_WATT,
    ELECTRICAL_VOLT_AMPERE,
    PERCENTAGE,
    VOLT,
    TEMP_CELSIUS,
)


DOMAIN = "sunpower"


SUNPOWER_OBJECT = "sunpower"
SUNPOWER_HOST = "host"
SUNPOWER_COORDINATOR = "coordinator"
UPDATE_INTERVAL = 120
SETUP_TIMEOUT_MIN = 5
# SUNPOWER_DATA = "data"

PVS_DEVICE_TYPE = "PVS"
INVERTER_DEVICE_TYPE = "Inverter"
METER_DEVICE_TYPE = "Power Meter"

PVS_STATE = "STATE"

METER_STATE = "STATE"

INVERTER_STATE = "STATE"

WORKING_STATE = "working"

METER_SENSORS = {
    "METER_FREQUENCY": ["freq_hz", "Frequency", FREQUENCY_HERTZ, "mdi:flash"],
    "METER_NET_KWH": [
        "net_ltea_3phsum_kwh",
        "Lifetime Power",
        ENERGY_KILO_WATT_HOUR,
        "mdi:flash",
    ],
    "METER_KW": ["p_3phsum_kw", "Power", POWER_KILO_WATT, "mdi:flash"],
    "METER_VAR": ["q_3phsum_kvar", "KVA Reactive", ELECTRICAL_VOLT_AMPERE, "mdi:flash"],
    "METER_VA": ["s_3phsum_kva", "KVA Apparent", ELECTRICAL_VOLT_AMPERE, "mdi:flash"],
    "METER_POWER_FACTOR": ["tot_pf_rto", "Power Factor", PERCENTAGE, "mdi:flash"],
}

INVERTER_SENSORS = {
    "INVERTER_NET_KWH": [
        "ltea_3phsum_kwh",
        "Lifetime Power",
        ENERGY_KILO_WATT_HOUR,
        "mdi:flash",
    ],
    "INVERTER_KW": ["p_3phsum_kw", "Power", POWER_KILO_WATT, "mdi:flash"],
    "INVERTER_VOLTS": ["vln_3phavg_v", "Voltage", VOLT, "mdi:flash"],
    "INVERTER_AMPS": ["i_3phsum_a", "Amps", ELECTRICAL_VOLT_AMPERE, "mdi:flash"],
    "INVERTER_MPPT_KW": ["p_mpptsum_kw", "MPPT KW", POWER_KILO_WATT, "mdi:flash"],
    "INVERTER_MPPT_V": ["v_mppt1_v", "MPPT Volts", VOLT, "mdi:flash"],
    "INVERTER_MPPT_A": ["i_mppt1_a", "MPPT Amps", ELECTRICAL_VOLT_AMPERE, "mdi:flash"],
    "INVERTER_TEMPERATURE": [
        "t_htsnk_degc",
        "Temperature",
        TEMP_CELSIUS,
        "mdi:temperature-celsius",
    ],
    "INVERTER_FREQUENCY": ["freq_hz", "Frequency", FREQUENCY_HERTZ, "mdi:flash"],
}

PVS_SENSORS = {
    "PVS_LOAD": ["dl_cpu_load", "System Load", "", "mdi:gauge"],
    "PVS_ERROR_COUNT": ["dl_err_count", "Error Count", "", "mdi:alert-circle"],
    "PVS_COMMUNICATION_ERRORS": [
        "dl_comm_err",
        "Communication Errors",
        "",
        "mdi:network-off",
    ],
    "PVS_SKIPPED_SCANS": [
        "dl_skipped_scans",
        "Skipped Scans",
        "",
        "mdi:network-strength-off-outline",
    ],
    "PVS_SCAN_TIME": ["dl_scan_time", "Scan Time", TIME_SECONDS, "mdi:timer-outline"],
    "PVS_UNTRANSMITTED": [
        "dl_untransmitted",
        "Untransmitted Data",
        "",
        "mdi:radio-tower",
    ],
    "PVS_UPTIME": ["dl_uptime", "Uptime", TIME_SECONDS, "mdi:timer-outline"],
    "PVS_MEMORY_USED": ["dl_mem_used", "Memory Used", DATA_KILOBYTES, "mdi:memory"],
    "PVS_FLASH_AVAILABLE": [
        "dl_flash_avail",
        "Flash Available",
        DATA_KILOBYTES,
        "mdi:memory",
    ],
}
