<a id="readme-top"></a>

[![License][license-shield]][license-url]

<br />
<div align="center">
  <h3 align="center">📡 Sentinel Agent</h3>

  <p align="center">
    An automated AI/tech intelligence pipeline — scrapes Twitter/RSS sources, filters and ranks with an LLM, and pushes a curated daily digest via Telegram.
    <br />
    <a href="https://github.com/Sentinel-0x/Sentinel-agent"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Sentinel-0x/Sentinel-agent/issues/new?labels=bug">Report Bug</a>
    ·
    <a href="https://github.com/Sentinel-0x/Sentinel-agent/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul><li><a href="#built-with">Built With</a></li></ul>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#architecture">Architecture</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

Keeping up with AI/tech news across Twitter and research feeds is a full-time job on its own. This project automates the loop: it pulls posts from a curated list of AI researchers and builders via RSS, scores and filters them with an LLM, formats the results into a readable digest, and pushes it straight to Telegram — so the daily update shows up without any manual browsing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python-badge]][Python-url]
* [![Telegram][Telegram-badge]][Telegram-url]
* [![Prometheus][Prometheus-badge]][Prometheus-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

* Python 3.10+
* A Telegram bot token (create one via [@BotFather](https://t.me/botfather))

### Installation

1. Clone the repo
```sh
   git clone https://github.com/Sentinel-0x/Sentinel-agent.git
   cd Sentinel-agent
```
2. Install dependencies
```sh
   pip install -r requirements.txt
```
3. Create a `.env` file with your configuration:
## Architecture

| Component | File | What it does |
|---|---|---|
| Intelligence Fetching | `tools.py` | `fetch_ai_intelligence()` — pulls posts from a curated list of AI researcher/builder Twitter handles via RSS/Nitter |
| Analysis | `analyzer.py` | Filters and scores raw items using an LLM |
| Formatting | `formatter.py` | `format_telegram_markdown()` — renders scored intelligence into a Telegram Markdown digest |
| Telegram Push | `push_telegram.py`, `daily_push.py` | Sends the formatted digest to Telegram, with retry logic (`tenacity`) |
| Job Registry / Sandbox Bridge | `tool_registry.py` | Bridges to [`sentinel-react-engine`](https://github.com/Sentinel-0x/sentinel-react-engine) for AST-checked, sandboxed dynamic code execution |
| Logging | `logger.py` | Rotating file logger (5MB cap) |
| Metrics | `metrics.py` | Prometheus counters for jobs processed / push errors |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] Multi-source intelligence fetching (Twitter/RSS)
- [x] LLM-based filtering and scoring
- [x] Telegram digest formatting and push
- [x] Prometheus metrics
- [x] Sandboxed dynamic tool execution via `sentinel-react-engine`
- [ ] Expand source coverage beyond current handles
- [ ] Add automated test coverage for the fetch/analyze pipeline

See the [open issues](https://github.com/Sentinel-0x/Sentinel-agent/issues) for a full list of proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Project Link: [https://github.com/Sentinel-0x/Sentinel-agent](https://github.com/Sentinel-0x/Sentinel-agent)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/Sentinel-0x/Sentinel-agent.svg?style=for-the-badge
[license-url]: https://github.com/Sentinel-0x/Sentinel-agent/blob/main/LICENSE
[Python-badge]: https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Telegram-badge]: https://img.shields.io/badge/Telegram-push%20notifications-26A5E4?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://telegram.org/
[Prometheus-badge]: https://img.shields.io/badge/Prometheus-metrics-E6522C?style=for-the-badge&logo=prometheus&logoColor=white
[Prometheus-url]: https://prometheus.io/

