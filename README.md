[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)

# HomeAssistant-GreeClimateComponent
Custom Gree climate component written in Python3 for Home Assistant. Controls AC's supporting the Gree protocol.

Tested on the following hardware:
- AC Pioneer Fortis Series with WI-FI module CS532AE
- AC Gree GWH12ACC-K6DNA1D
- AC Gree 3VIR24HP230V1AH
- Argo ECOLIGHT 9000 UI WF - Split Air Conditioner Unit (Pair through EWPE Smart app, default settings in gree are fine)
- Argo ECOLIGHT 12000 UI WiFi - Split Air Conditioner Unit (Pair through EWPE Smart app, default settings in gree are fine)
- Bulex vivair multisplit units; 20-080MC4NO outdoor unit, 20-025 NWI (2,5 kW) indoor unit, 20-035 NWI (3,5 kW) indoor unit
- CASCADE BORA-CWH09AAB
- Cooper & Hunter (CH-S12FTXE(WI-FI)-NG)
- Copmax Air-Air Heatpump GWH12QC-K6DNA5F 3.5kW
- EWT S-090 GDI-HRFN1, EWT S-120 GDI-HRFN1 (WI-FI module CS532AEH)
- Innova HVAC
- Inventor Life Pro WiFi
- Kinghome "Pular" - KW12HQ25SDI (Requires encryption_version=2)
- Kolin KAG-100WCINV (Requires encryption_version=2)
- Kolin KAG-145WCINV (Requires encryption_version=2)
- Saunier Duval VivAir Lite SDHB1-025SNWI (Requires encryption_version=2)
- Saunier Duval VivAir Lite SDHB1-035SNWI (Requires encryption_version=2)
- Sinclair ASH-12BIV
- Sinclair ASH-13BIF2
- Sinclair SIH-09BITW
- Tadiran Alpha Expert Inverter
- TOSOT BORA-GWH09AAB
- TOSOT TW12HXP2A1D
- Toyotomi Izuru TRN/TRG-828ZR
- Wilfa Cool9 Connected

Tested on Home Assistant 2025.6.3 

**If you are experiencing issues please be sure to provide details about your device, Home Assistant version and what exactly went wrong.**

 If your HVAC has already been configured to be controlled remotely by an android app, the encryption key might have changed.

 To configure HVAC wifi (without the android app): https://github.com/arthurkrupa/gree-hvac-mqtt-bridge#configuring-hvac-wifi

**Sources used:**
 - https://github.com/tomikaa87/gree-remote
 - https://github.com/vpnmaster/homeassistant-custom-components
 - https://developers.home-assistant.io/

## HACS
This component is added to HACS default repository list.

## UI Configuration
The integration can be added from the Home Assistant UI.
1. Navigate to **Settings** > **Devices & Services** and click **Add Integration**.
2. Search for **Gree Climate** and fill in the host, port and MAC address.
3. After setup you can open the integration options to configure additional parameters.
4. Saving any changes in the options dialog automatically reloads the
   integration, so new settings take effect immediately without
   restarting Home Assistant.

## Custom Component Installation
!!! PLEASE NOTE !!!: Skip step 1 if you are using HACS.

1. Copy the custom_components folder to your own hassio /config folder.

2. In the root of your /config folder, create a file called climate.yaml.

   ```yaml
   - platform: gree
     name: First AC
     host: 192.168.1.101
     port: 7000
     mac: 20fabb123456

   - platform: gree
     name: Second AC
     host: 192.168.1.102
     port: 7000
     mac: 20fabb123423
   ```
   You can configure additional parameters from the table below to fit the features that your AC supports.

   | Parameter | Description | Value | Required | Default |
   | --------- | ----------- | ------ | -------- | ------- |
   | `name` | Name | `string` (e.g., `First AC`) | `false` | `Gree Climate` |
   | `host` | IP Address of AC | `string` (e.g., `192.168.1.101`) | `true` | |
   | `port` | Port number to connect to the device | `integer` (e.g., `7000`) | `false` | `7000` |
   | `mac` | MAC address of the device | `string` (e.g., `20fabb123456`) <br> **NOTE: Format can be XX:XX:XX:XX:XX:XX, XX-XX-XX-XX-XX-XX or xxxxxxxxxxxx depending on your model** | `true` | 
   | `encryption_key` | Custom encryption key | `string` (e.g., `A1B2C3D4E5F6`) | `false` | *(auto-fetched if empty)* |
   | `encryption_version` | Encryption version | `integer` (e.g., `2`) | `false` | `1` | |
   | `hvac_modes` | Standard Home Assistant HVAC Modes to enable | `list[string]` (e.g. `["auto", "cool", "dry", "fan_only", "off"]`) | `false` | `["auto", "cool", "dry", "fan_only", "heat", "heat_cool", "off"]` |
   | `fan_modes` | Fan modes | `list[string]` (e.g. `["auto", "low", "medium", "high"]`) | `false` | `["auto", "low", "medium_low", "medium", "medium_high", "high", "turbo", "quiet"]` |
   | `swing_modes` | Fan vertical swing modes | `list[string]` (e.g. `["default", "swing_full"]`) <br> **NOTE: Pass empty list (`[]`) to disable vertical swing** | `false` | `["default", "swing_full", "fixed_upmost", "fixed_middle_up", "fixed_middle", "fixed_middle_low", "fixed_lowest", "swing_downmost", "swing_middle_low", "swing_middle", "swing_middle_up", "swing_upmost"]` |
   | `swing_horizontal_modes` | Fan horizontal swing modes | `list[string]` (e.g. `["default", "swing_full"]`) <br> **NOTE: Pass empty list (`[]`) to disable horizontal swing** | `false` | `["default", "swing_full", "fixed_leftmost", "fixed_middle_left", "fixed_middle", "fixed_middle_right", "fixed_rightmost"]` |
   | `target_temp_step` | Temperature adjustment step | `integer` (e.g., `1`) | `false` | `1` |
   | `uid` | Device identifier | `string` (e.g., `AC_UNIT_123`) | `false` | |
   | `temp_sensor` | External temp sensor entity ID | `entity_id` (e.g., `sensor.bedroom_temperature`) | `false` | |
   | `lights` | AC lights mode toggle | `input_boolean` (e.g., `input_boolean.first_ac_lights`) | `false` | |
   | `xfan` | xFan mode toggle | `input_boolean` (e.g., `input_boolean.first_ac_xfan`) | `false` | |
   | `health` | Health option toggle | `input_boolean` (e.g., `input_boolean.first_ac_health`) | `false` | |
   | `sleep` | Sleep mode toggle | `input_boolean` (e.g., `input_boolean.first_ac_sleep`) | `false` | |
   | `powersave` | Powersave mode toggle | `input_boolean` (e.g., `input_boolean.first_ac_powersave`) | `false` | |
   | `eightdegheat` | 8°C heating mode toggle | `input_boolean` (e.g., `input_boolean.first_ac_eightdegheat`) | `false` | |
   | `air` | Air/scavenging toggle | `input_boolean` (e.g., `input_boolean.first_ac_air`) | `false` | |
   | `target_temp` | External temperature control | `input_number` (e.g., `input_number.bedroom_temp_target`) | `false` | |
   | `auto_xfan` | Auto xFan in cool/dry mode | `input_boolean` (e.g., `input_boolean.auto_xfan`) | `false` | |
   | `auto_light` | Auto control for AC light | `input_boolean` (e.g., `input_boolean.auto_light`) | `false` | |
   | `anti_direct_blow` | Anti Direct Blow feature toggle | `input_boolean` (e.g., `input_boolean.anti_direct_blow`) | `false` | |
   | `light_sensor` | Enable built-in light sensor | `input_boolean` (e.g., `input_boolean.enable_light_sensor`) | `false` | |
   | `max_online_attempts` | Retry limit before marking unavailable | `integer` (e.g., `5`) | `false` | `3` |
   | `disable_available_check` | Keep AC always available in HA | `boolean` (e.g., `true`) | `false` | `false` |
   | `temp_sensor_offset` | Display offset for temp sensor | `boolean` (e.g., `true`) | `false` | *(auto-detected if not set)* |
   | `beeper` | Toggle beeping sounds | `input_boolean` (e.g., `input_boolean.first_ac_beeper`) | `false` | |


3. In your configuration.yaml add the following:

   ```yaml
   climate: !include climate.yaml
   ```

4. OPTIONAL: Add info logging to this component (to see if/how it works)

   ```yaml
   logger:
     default: error
     logs:
       custom_components.gree: debug
       custom_components.gree.climate: debug
   ```

5. OPTIONAL: Provide encryption key if you have it or feel like extracting it.

   One way is to pull the sqlite db from android device like described here:

   https://stackoverflow.com/questions/9997976/android-pulling-sqlite-database-android-device

   ```
   adb backup -f ~/backup.ab -noapk com.gree.ewpesmart
   dd if=data.ab bs=1 skip=24 | python -c "import zlib,sys;sys.stdout.write(zlib.decompress(sys.stdin.read()))" | tar -xvf -
   sqlite3 data.ab 'select privateKey from db_device_20170503;' # but table name can differ a little bit.
   ```

   Write it down in climate.yaml `encryption_key: <key>`.

6. OPTIONAL: Provide the `uid` parameter (can be sniffed) NOTE: This is not needed for all devices

7. OPTIONAL: Provide input_boolean's to set lights, xfan, sleep and powersave mode on/off.

8. OPTIONAL: You can set custom icons by modifying the icon translation file `icons.json`. Refer to this documentation: https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/icon-translations/

## Optional Features
NOTE: Your AC has to support these features for it to be used.
```
     temp_sensor: This attaches an external temperature sensor to your AC. Gree unfortunately doesnt support a "current temperature" on its own.
     lights: This switches the backlight of the AC Display on or off
     xfan: This dries the AC after being used. This is to avoid nasty smells from usage.
     health: The air goes through a filter to "clean the air".
     sleep: This will enable a comfortable sleep mode. The AC won't make a lot of noise using this.
     powersave: It seems this mode should be an efficient way of approximately reaching the desired temperature (temperatures will vary using this).
     eightdegheat:  This feature maintains the room temperature steadily at 8°C and prevents the room from freezing by activating the heating operation automatically when nobody is at home over a longer period during severe winter
     air: This feature will extract air from the room. This is to remove hot air or nasty smells from the room.
     target_temp: You can use a custom input_number entity as the input of the set temperature for this AC. Define the input_number entity in this parameter. This is useful if you want to use dashboards with custom frontend components.
     auto_xfan: This feature will always turn on xFan in cool and dry mode to avoid mold & rust created from potential water buildup in the AC
     auto_light: This feature will always turn light on when power on and turn light light off when power off automatically
```
