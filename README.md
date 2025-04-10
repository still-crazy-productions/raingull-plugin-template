# RainGull Plugin Template

**Version:** 0.2  
**Author:** Your Name (GitHub link)  
**License:** MIT License  

---

## ✅ Overview

This repository provides a **clearly documented**, standardized template for developing plugins for RainGull, a flexible, lightweight communication relay system.

Plugins developed using this template clearly define how RainGull interacts with external messaging Platforms (email, SMS, Telegram, Discord, etc.). Plugins may handle incoming messages, outgoing messages, or both.

---

## 🗂️ Plugin Structure

Use the following recommended directory structure clearly when developing your plugin:

```
raingull-plugin-example/
├── manifest.json         # Plugin metadata & configuration schema
├── README.md             # Documentation for the plugin
├── LICENSE               # License file
├── forms.py              # Django forms for configuration
├── handlers.py           # Platform-specific message handling logic
├── translate.py          # Message translation logic (to/from RainGull)
├── models.py             # Django models (optional, but recommended)
└── tests/
    └── test_plugin.py    # Tests for your plugin logic
```

---

## 🆔 RainGull Message ID (`raingull_id`)

Every message processed by a plugin must clearly include a unique RainGull Message ID (`raingull_id`), which remains consistent throughout the lifecycle of the message:

- For incoming messages, assign a new UUID (`uuid.uuid4`) immediately upon retrieval.
- For outgoing messages, reuse the existing UUID from the standardized RainGull message.

### Example Implementation:

```python
import uuid

# Incoming Message example
new_message = PluginIncomingMessage(
    raingull_id=uuid.uuid4(),
    raw_message=platform_data
)
new_message.save()

# Outgoing Message example
outgoing_message = PluginOutgoingMessage(
    raingull_id=standardized_message["raingull_id"],
    formatted_message=platform_specific_data
)
outgoing_message.save()
```

---

## ✂️ Message Snippets

Plugins must generate a short "Snippet" from the message body. Snippets provide a quick preview of message content, particularly valuable for brief notifications or SMS alerts.

- Clearly recommended default length: **200 characters**
- Configurable via the plugin's manifest and admin settings (optional)

### Example Snippet Generation:

```python
body = raw_message["body"]
snippet_length = config.get("snippet_length", 200)

snippet = body[:snippet_length] + "..." if len(body) > snippet_length else body
```

---

## 🔧 Installation & Activation

Clearly explain how admins can install and activate this plugin in RainGull:

1. Clone or download the repository.
2. Copy the plugin folder into your RainGull plugins directory.
3. Activate the plugin via the RainGull admin interface.
4. Configure required settings as defined clearly in `manifest.json`.

---

## 📑 Plugin Configuration (`manifest.json`)

The `manifest.json` clearly defines your plugin configuration options.

| Setting             | Description                                 | Required | Default     |
|---------------------|---------------------------------------------|----------|-------------|
| `service_name`      | Unique identifier for the service instance  | Yes      | n/a         |
| `platform_server`   | URL of Platform server (e.g., IMAP server)  | Yes      | n/a         |
| `platform_port`     | Port number                                 | Yes      | 443         |
| `encryption`        | SSL/TLS encryption type                     | Yes      | SSL/TLS     |
| `platform_username` | Username for Platform (optional)            | No       | n/a         |
| `platform_password` | Password for Platform (optional)            | No       | n/a         |
| `poll_frequency`    | Frequency of checking messages (minutes)    | No       | 5           |
| `snippet_length`    | Length of the generated snippet (chars)     | No       | 200         |

---

## 📥 Incoming Message Handling

If your plugin handles incoming messages:

- Clearly document how the plugin retrieves data from the Platform.
- Clearly specify the structure of raw incoming messages.
- Clearly define how raw messages are stored, including generating the required UUID (`raingull_id`) and message snippet.

---

## 📤 Outgoing Message Handling

If your plugin handles outgoing messages:

- Clearly document how your plugin formats outgoing messages.
- Specify if your plugin supports full messages, snippets, or both.
- Clearly describe any platform-specific considerations or limitations.

---

## 🚩 Troubleshooting

Document clearly any common errors, issues, or troubleshooting steps.

Example:

- **Connection issues:** Verify credentials and server availability using the "Test Connection" button provided in RainGull’s admin UI.

---

## 🧪 Testing

Clearly describe or provide automated tests for your plugin logic in the included `tests` folder.  
A clear example structure is provided in the template repository (`tests/test_plugin.py`).

---

## 🤝 Contributing

We warmly encourage clear, helpful contributions:

1. Fork this repository clearly.
2. Clearly make your changes or enhancements.
3. Open a clearly documented Pull Request against the original repository.

---

## 📜 License

This project is clearly licensed under the MIT License. See `LICENSE` file for details.

---

## 🎯 Ready to get started?

This template clearly defines best practices for plugin creation, maintaining consistency and clarity throughout RainGull’s plugin ecosystem.  

Fork or clone this repo to start building your own RainGull plugins!

