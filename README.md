# Self-Healing Infrastructure with Prometheus, NGINX, and Docker

## 🚀 Introduction
This project demonstrates how to set up a **self-healing infrastructure** using **Prometheus**, **NGINX**, **Docker**, and **Ansible**. The system continuously monitors NGINX for any downtime and automatically restarts it when necessary. Additionally, Prometheus and Alertmanager are used for monitoring and alerting, ensuring the system's health is actively tracked.

## 🛠️ Technologies Used
- **Docker** for containerization of services.
- **Prometheus** for monitoring metrics and alerting.
- **NGINX** as the web server.
- **NGINX Prometheus Exporter** for exporting NGINX metrics.
- **Alertmanager** to handle alert notifications.
- **Ansible** for automating the self-healing process (restarting services when necessary).

## 🔧 Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Docker
- Docker Compose
- Ansible (for automation)

### 📂 Project Structure
.
├── alerts/                     # Prometheus alert rules
├── config/                     # Prometheus & Alertmanager configs
├── heal-nginx.yml              # Ansible playbook for self-healing
├── webhook_listener.py         # Custom webhook listener
├── docker-compose.yml          # Service orchestration
├── logs/                       # Collected logs
└── README.md                   # This file

### Steps to Set Up

1. **Clone this repository**:

     ```
     git clone https://github.com/viqarkaif/self-healing-infra-P1-.git
     ```
    ```
     cd self-healing-infra
    ```

3. **Start the services using Docker Compose**:

    ```
    docker-compose up -d
   ```

5. **Configure Prometheus**:
   
    - Prometheus is configured to scrape metrics from the **NGINX Prometheus Exporter** at port `9113`.

6. **Set up Alertmanager**
   
    - Alerts are configured to trigger when NGINX goes down. Check the **Alertmanager UI** at `http://localhost:9093` for alert details.

8. **Self-Healing with Ansible**:
   
    - The playbook `heal-nginx.yml` is responsible for automatically restarting the NGINX and Exporter containers if they go down.


## 🧪 Testing the Self-Healing

**1. Stop NGINX container:**

      docker stop nginx
   
**2. Watch Prometheus alert fire**

**3. Observe webhook triggers Ansible**

**4. NGINX & Exporter automatically restart 🎉**

  

## 🧱 Architecture          

```mermaid                
graph TD;                
  NGINX-->Exporter;        
  Exporter-->Prometheus;   
  Prometheus-->Alertmanager;
  Alertmanager-->Webhook;   
  Webhook-->Ansible;        
  Ansible-->Docker;          
```                     


### 🖼️ Screenshots

### Docker starting status
![Screenshot 2025-04-25 045517](https://github.com/user-attachments/assets/b32c7ef6-e6d7-4c5a-a577-831a0884f70a)

### Files content
![Screenshot 2025-04-25 045633](https://github.com/user-attachments/assets/e24b512c-c11b-4d2c-b792-497a93bd57eb)

#### Prometheus Targets Page
![prometheus_targets](https://github.com/user-attachments/assets/bca8f3c5-d5a6-4de5-a6cb-4c1cc3ed863c)

![Screenshot 2025-04-25 045757](https://github.com/user-attachments/assets/cf46d770-7388-4163-8de4-ef129fe42f00)
    
### Auto Healing triggered when Nginx is stopped
![Screenshot 2025-04-25 050015](https://github.com/user-attachments/assets/db4f0a1d-fe81-4b91-86d6-8997ed4c259e)

### Ater Nginx Stopped ---> Prometheus Targets Page (Showing Nginx is Down)
![Screenshot 2025-04-25 050057](https://github.com/user-attachments/assets/23d6a2a1-bbfb-4fee-88c4-4d509416b6c2)

![Screenshot 2025-04-25 050127](https://github.com/user-attachments/assets/b12fe18c-9f43-443e-9d62-5c7507d1b731)

#### Prometheus Alerting Page
![Screenshot 2025-04-25 050140](https://github.com/user-attachments/assets/a76f53a3-150f-4f65-a9cc-3f0da27c3081)

### Alert Successfully Triggered
![Screenshot 2025-04-25 050210](https://github.com/user-attachments/assets/8a6e2672-4d48-4303-af75-f03b98de74a1)

### Alert Manager Recieved the Alert Request
![Screenshot 2025-04-25 050317](https://github.com/user-attachments/assets/abb78eae-58e7-46e3-92a4-cf2104c557be)

### Ansible Started Auto Healing by Executing the Ansible Playbook the Heal-Nginx.yml 
![Screenshot 2025-04-25 050506](https://github.com/user-attachments/assets/98383a25-c4b1-4b0b-847e-b0c8def6778d)

#### Docker Status After Nginx is Healed Successfully
![Screenshot 2025-04-25 050514](https://github.com/user-attachments/assets/91656641-d158-4491-9c2a-0c83b2c3ebdd)

### Prometheus Monitered the Nginx Status After it healed
![Screenshot 2025-04-25 050654](https://github.com/user-attachments/assets/dc1ca547-d3a3-4206-8743-b01ffc6a562d)


#### Docker Compose File
![Screenshot 2025-04-25 050810](https://github.com/user-attachments/assets/a78bdc57-c958-4aed-94d3-ecdb5b64ab6a)


### 🚨 Troubleshooting

- **NGINX is not responsive**: If NGINX is not responding, the **self-healing playbook** will automatically restart the NGINX container.
- **Exporter is down**: If the NGINX Prometheus Exporter is down, ensure that the Docker container is running. You can restart it using the Ansible playbook.

## 📚 Tools Used

1. Prometheus

2. Alertmanager

3. Ansible

4. Docker & Docker Compose

5. Python (Webhook listener)

## 🧑‍💻 Conclusion
This project ensures your infrastructure is resilient and self-healing. Using Prometheus and Alertmanager for monitoring, and Ansible for automation, this setup guarantees minimal downtime and automated recovery for critical services like NGINX.


---
## 📬 Author

.🔗 LinkedIn 

.🧑‍💻 GitHub: @viqarkaif
