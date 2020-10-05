"""Support for Sunpower binary sensors."""
import logging

from homeassistant.const import DEVICE_CLASS_POWER

from .const import (
    DOMAIN,
    SUNPOWER_COORDINATOR,
    #    SUNPOWER_DATA,
    #    SUNPOWER_OBJECT,
    PVS_DEVICE_TYPE,
    INVERTER_DEVICE_TYPE,
    METER_DEVICE_TYPE,
    PVS_STATE,
    METER_STATE,
    INVERTER_STATE,
    WORKING_STATE,
)
from .entity import SunPowerPVSEntity, SunPowerMeterEntity, SunPowerInverterEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Sunpower sensors."""
    sunpower_state = hass.data[DOMAIN][config_entry.entry_id]
    _LOGGER.error("Sunpower_state: %s", sunpower_state)

    coordinator = sunpower_state[SUNPOWER_COORDINATOR]
    sunpower_data = coordinator.data

    if PVS_DEVICE_TYPE not in sunpower_data:
        _LOGGER.error("Cannot find PVS Entry")
    else:
        pvs = next(iter(sunpower_data[PVS_DEVICE_TYPE].values()))

        entities = [SunPowerPVSState(coordinator, pvs)]

        if METER_DEVICE_TYPE not in sunpower_data:
            _LOGGER.error("Cannot find any power meters")
        else:
            for data in sunpower_data[METER_DEVICE_TYPE].values():
                entities.append(SunPowerMeterState(coordinator, data, pvs))

        if INVERTER_DEVICE_TYPE not in sunpower_data:
            _LOGGER.error("Cannot find any power inverters")
        else:
            for data in sunpower_data[INVERTER_DEVICE_TYPE].values():
                entities.append(SunPowerInverterState(coordinator, data, pvs))

    async_add_entities(entities, True)


class SunPowerPVSState(SunPowerPVSEntity):
    """Representation of SunPower PVS Working State"""

    @property
    def name(self):
        """Device Name."""
        return "System State"

    @property
    def device_class(self):
        """Device Class."""
        return DEVICE_CLASS_POWER

    @property
    def unique_id(self):
        """Device Uniqueid."""
        return f"{self.base_unique_id}_pvs_state"

    @property
    def state(self):
        """Get the current value"""
        return self._pvs_info[PVS_STATE]

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return self.state == WORKING_STATE


class SunPowerMeterState(SunPowerMeterEntity):
    """Representation of SunPower Meter Working State"""

    @property
    def name(self):
        """Device Name."""
        return "System State"

    @property
    def device_class(self):
        """Device Class."""
        return DEVICE_CLASS_POWER

    @property
    def unique_id(self):
        """Device Uniqueid."""
        return f"{self.base_unique_id}_meter_state"

    @property
    def state(self):
        """Get the current value"""
        return self._meter_info[METER_STATE]

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return self.state == WORKING_STATE


class SunPowerInverterState(SunPowerInverterEntity):
    """Representation of SunPower Inverter Working State"""

    @property
    def name(self):
        """Device Name."""
        return "System State"

    @property
    def device_class(self):
        """Device Class."""
        return DEVICE_CLASS_POWER

    @property
    def unique_id(self):
        """Device Uniqueid."""
        return f"{self.base_unique_id}_inverter_state"

    @property
    def state(self):
        """Get the current value"""
        return self._inverter_info[INVERTER_STATE]

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return self.state == WORKING_STATE
