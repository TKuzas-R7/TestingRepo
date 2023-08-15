# Description

Encode and decode data using the base64 alphabet

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
*This plugin does not contain any supported product versions.*

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Decoder
  
Decode Base64 to data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|base64|bytes|None|True|Data to decode|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cgo=|
|errors|string|nothing|False|How errors should be handled when decoding Base64|['replace', 'ignore', 'nothing']|ignore|
  
Example input:

```
{
  "base64": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cgo=",
  "errors": "nothing"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|string|True|Decoded data result|None|
  
Example output:

```
{
  "data": ""
}
```

#### Encoder
  
Encode data to Base64

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|content|string|None|True|Data to encode|None|Rapid7 InsightConnect|
  
Example input:

```
{
  "content": "Rapid7 InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|bytes|True|Encoded data result|None|
  
Example output:

```
{
  "data": ""
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History
  
*This plugin does not contain a version history.*

# Links


## References
  
*This plugin does not contain any references.*