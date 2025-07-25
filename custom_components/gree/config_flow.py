"""Config flow for Gree climate integration."""

from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector
from homeassistant.const import (
    CONF_HOST,
    CONF_MAC,
    CONF_NAME,
    CONF_PORT,
    CONF_TIMEOUT,
)
from homeassistant.data_entry_flow import FlowResult

_LOGGER = logging.getLogger(__name__)

from .const import *
class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Gree climate."""

    VERSION = 1

    def __init__(self) -> None:
        self._data: dict[str, any] = {}

    async def async_step_user(self, user_input: dict | None = None) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            self._data.update(user_input)
            return self.async_create_entry(
                title=user_input.get(CONF_NAME) or "Gree Climate", data=self._data
            )

        data_schema = vol.Schema(
            {
                vol.Required(CONF_HOST): str,
                vol.Required(CONF_MAC): str,
                vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
                vol.Optional(CONF_NAME): str,
                vol.Optional(CONF_TIMEOUT, default=DEFAULT_TIMEOUT): int,
                vol.Optional(CONF_ENCRYPTION_KEY): str,
                vol.Optional(CONF_UID): int,
                vol.Optional(CONF_ENCRYPTION_VERSION, default=1): int,
            }
        )
        return self.async_show_form(step_id="user", data_schema=data_schema)

    async def async_step_import(self, import_data: dict) -> FlowResult:
        """Handle configuration via YAML import."""
        return await self.async_step_user(import_data)

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        return OptionsFlowHandler(config_entry)


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle an options flow for Gree climate."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(self, user_input: dict | None = None) -> FlowResult:
        if user_input is not None:
            _LOGGER.debug("Raw user options input: %s", user_input)
            normalized_input: dict[str, str | None] = {}
            # Only handle known option keys
            for key in OPTION_KEYS:
                if key in user_input:
                    value = user_input[key]
                    normalized_input[key] = value if value not in (None, "") else None
                elif key in self.config_entry.options:
                    normalized_input[key] = None
            _LOGGER.debug("Normalized options to save: %s", normalized_input)
            result = self.async_create_entry(title="", data=normalized_input)
            _LOGGER.debug("Creating entry with options: %s", normalized_input)
            return result

        options = {
            key: value
            for key, value in self.config_entry.options.items()
            if key in OPTION_KEYS
        }
        _LOGGER.debug("Current stored options: %s", options)
        schema = vol.Schema(
            {
                vol.Optional(
                    CONF_HVAC_MODES,
                    description={"suggested_value": options.get(
                        CONF_HVAC_MODES, DEFAULT_HVAC_MODES
                    )},
                    default=options.get(
                        CONF_HVAC_MODES, DEFAULT_HVAC_MODES
                    ),
                ): vol.Any(
                    None,
                    selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=DEFAULT_HVAC_MODES,
                            multiple=True,
                            custom_value=True,
                            translation_key=CONF_HVAC_MODES
                        )
                    )
                ),
                vol.Optional(
                    CONF_TARGET_TEMP_STEP,
                    default=options.get(
                        CONF_TARGET_TEMP_STEP, DEFAULT_TARGET_TEMP_STEP
                    ),
                ): vol.Coerce(float),
                vol.Optional(
                    CONF_TEMP_SENSOR,
                    description={"suggested_value": options.get(CONF_TEMP_SENSOR)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="sensor")
                    ),
                ),
                vol.Optional(
                    CONF_LIGHTS,
                    description={"suggested_value": options.get(CONF_LIGHTS)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_XFAN,
                    description={"suggested_value": options.get(CONF_XFAN)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_HEALTH,
                    description={"suggested_value": options.get(CONF_HEALTH)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_POWERSAVE,
                    description={"suggested_value": options.get(CONF_POWERSAVE)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_SLEEP,
                    description={"suggested_value": options.get(CONF_SLEEP)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_EIGHTDEGHEAT,
                    description={"suggested_value": options.get(CONF_EIGHTDEGHEAT)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_AIR,
                    description={"suggested_value": options.get(CONF_AIR)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_TARGET_TEMP,
                    description={"suggested_value": options.get(CONF_TARGET_TEMP)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_number")
                    ),
                ),
                vol.Optional(
                    CONF_AUTO_XFAN,
                    description={"suggested_value": options.get(CONF_AUTO_XFAN)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_AUTO_LIGHT,
                    description={"suggested_value": options.get(CONF_AUTO_LIGHT)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_FAN_MODES,
                    description={"suggested_value": options.get(
                        CONF_FAN_MODES, DEFAULT_FAN_MODES
                    )},
                    default=options.get(
                        CONF_FAN_MODES, DEFAULT_FAN_MODES
                    ),
                ): vol.Any(
                    None,
                    selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=DEFAULT_FAN_MODES,
                            multiple=True,
                            custom_value=True,
                            translation_key=CONF_FAN_MODES
                        )
                    )
                ),
                vol.Optional(
                    CONF_SWING_MODES,
                    description={"suggested_value": options.get(
                        CONF_SWING_MODES, DEFAULT_SWING_MODES
                    )},
                    default=options.get(
                        CONF_SWING_MODES, DEFAULT_SWING_MODES
                    ),
                ): vol.Any(
                    None,
                    selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=DEFAULT_SWING_MODES,
                            multiple=True,
                            custom_value=True,
                            translation_key=CONF_SWING_MODES
                        )
                    )
                ),
                vol.Optional(
                    CONF_SWING_HORIZONTAL_MODES,
                    description={"suggested_value": options.get(
                        CONF_SWING_HORIZONTAL_MODES, DEFAULT_SWING_HORIZONTAL_MODES
                    )},
                    default=options.get(
                        CONF_SWING_HORIZONTAL_MODES, DEFAULT_SWING_HORIZONTAL_MODES
                    ),
                ): vol.Any(
                    None,
                    selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=DEFAULT_SWING_HORIZONTAL_MODES,
                            multiple=True,
                            custom_value=True,
                            translation_key=CONF_SWING_HORIZONTAL_MODES
                        )
                    )
                ),
                vol.Optional(
                    CONF_ANTI_DIRECT_BLOW,
                    description={"suggested_value": options.get(CONF_ANTI_DIRECT_BLOW)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_DISABLE_AVAILABLE_CHECK,
                    default=options.get(CONF_DISABLE_AVAILABLE_CHECK, False),
                ): bool,
                vol.Optional(
                    CONF_MAX_ONLINE_ATTEMPTS,
                    default=options.get(CONF_MAX_ONLINE_ATTEMPTS, 3),
                ): int,
                vol.Optional(
                    CONF_LIGHT_SENSOR,
                    description={"suggested_value": options.get(CONF_LIGHT_SENSOR)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_BEEPER,
                    description={"suggested_value": options.get(CONF_BEEPER)},
                ): vol.Any(
                    None,
                    selector.EntitySelector(
                        selector.EntitySelectorConfig(domain="input_boolean")
                    ),
                ),
                vol.Optional(
                    CONF_TEMP_SENSOR_OFFSET,
                    description={"suggested_value": options.get(CONF_TEMP_SENSOR_OFFSET)},
                ): vol.Any(None, bool),
            }
        )
        return self.async_show_form(step_id="init", data_schema=schema)
