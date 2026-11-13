
# Industrial Automation and Workflow Integration

An engineering portfolio exploring the integration of industrial automation, intelligent production systems, industrial data, and digital workflow automation.

## About This Portfolio

This portfolio demonstrates how industrial equipment, control systems, software applications, and digital workflows can work together to improve manufacturing operations.

The projects combine practical industrial automation concepts with software-based solutions for machine monitoring, production planning, fault management, maintenance coordination, and operational data processing.

The objective is to bridge the gap between physical industrial processes and intelligent digital workflows.


## Project Portfolio

### Project A — Intelligent Machine Fault and Recovery Management


The system detects machine fault events through a TwinCAT PLC, transfers them using Python and MQTT, and processes them through n8n. It automatically creates and manages incident records in Airtable, prevents duplicate alerts, and sends fault and recovery notifications through Gmail.


**Key technologies:** TwinCAT, Structured Text, Python, pyads, MQTT, EMQX Cloud, n8n, Airtable, Gmail.

**Focus areas:** Machine monitoring, fault detection, event-driven communication, incident management, workflow automation.

**Status:** Core implementation completed and functionally tested.

### Project B — Digital Production Planning and Intelligent Laser-Cutting Operations

A simulated laser-cutting production environment combining machine operations, production planning, capacity management, and performance monitoring.

The system will process production orders, calculate material requirements, estimate processing times, monitor machine capacity, and identify production interruptions and delivery risks.

**Focus areas:** Industrial automation, production planning, machine data, manufacturing analytics, workflow integration.

**Status:** Design and development in progress.

### Project C — AI-Assisted Maintenance Coordination

An intelligent maintenance workflow that combines equipment events with maintenance history to support maintenance prioritisation and coordination.

The system will analyse equipment information, estimate potential downtime, prepare work orders, notify technicians, and propose maintenance scheduling options.

**Focus areas:** AI-assisted decision support, maintenance coordination, predictive insights, workflow automation.

**Status:** Planned 


## Technology Stack

| Area | Technologies |
|---|---|
| PLC and Industrial Automation | Beckhoff TwinCAT, Structured Text, EtherCAT |
| Industrial Communication | ADS, MQTT, Mosquitto, EMQX Cloud |
| Programming | Python |
| Workflow Automation | n8n |
| Data Management | Airtable |
| AI and Integration | OpenAI API, REST APIs, Webhooks |
| Monitoring and Visualisation | InfluxDB, Grafana |
| Development Tools | VS Code, Git, GitHub, Jupyter Notebook |


*The technologies listed represent tools currently used, under implementation, or planned across the portfolio projects.*


## Engineering Approach

The portfolio follows an integration-oriented approach:

1. **Control:** Use PLC-based automation to represent and control industrial processes.
2. **Connect:** Exchange machine and operational data through industrial communication protocols.
3. **Process:** Use Python and other software components to interpret and transform data.
4. **Automate:** Connect operational events to digital workflows and business applications.
5. **Improve:** Use monitoring, analytics, and AI-assisted insights to support better operational decisions.

## Repository Structure

```text
Industrial-Automation-and-Workflow-Integration/
│
├── Project A - Automated Fault Response Project/
│   ├── python_integration/
│   ├── plc/
│   ├── n8n/
│   ├── docs/
│   └── screenshots/
│
├── Project B - Digital Production Planning/
│   ├── plc/
│   ├── production_planning/
│   ├── workflow_automation/
│   ├── docs/
│   └── screenshots/
│
├── Project C - AI-Assisted Maintenance/
│   ├── ai_maintenance/
│   ├── workflow_automation/
│   ├── docs/
│   └── screenshots/
│
├── shared/
├── .gitignore
└── README.md
```

*Note: The structure represents the intended portfolio organisation. Some directories will be added as the projects develop.*

## Portfolio Objectives

- Demonstrate the connection between physical industrial processes and digital systems.
- Apply industrial communication protocols to machine-data exchange.
- Integrate PLC systems with Python-based applications.
- Develop event-driven workflows for operational response and coordination.
- Explore production planning, performance monitoring, and maintenance intelligence.
- Build practical engineering solutions that combine automation, software, and data.

## Development Philosophy

Each project is developed incrementally, with emphasis on understanding the engineering principles, implementing functional solutions, testing system behaviour, and documenting the results.

The overall goal is to demonstrate not only individual technical skills but also the ability to integrate different technologies into coherent industrial solutions.
