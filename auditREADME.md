# 🛠️ Netfix – Home Services Web Platform

Netfix is a Django-based web application that allows users to either **request home services** (Customers) or **offer them** (Companies). The platform supports full registration, service management, and request tracking functionalities.

---

## 🚀 Functional Requirements Checklist

### ✅ User Registration

#### 🧍 Customer
- Must provide:
  - **Username**
  - **Email**
  - **Password**
  - **Password Confirmation**
  - **Date of Birth**
- Registration must validate:
  - Unique **username**
  - Unique **email**

#### 🏢 Company
- Must provide:
  - **Username**
  - **Email**
  - **Password**
  - **Password Confirmation**
  - **Field of Work**
- Registration must validate:
  - Unique **username**
  - Unique **email**
  - Field of Work restricted to one of:
    ```
    Air Conditioner, All in One, Carpentry, Electricity,
    Gardening, Home Machines, Housekeeping, Interior Design,
    Locks, Painting, Plumbing, Water Heaters
    ```

### 🔐 Authentication
- Users (both types) must be able to **register** and **log in** using **email + password**.
- After login:
  - **Customer**: can view profile with personal info and service history
  - **Company**: can view profile with business info and created services

---

## 📦 Services

### 📍 Creation (Company only)
- Requires:
  - Name
  - Description
  - Price per hour
  - Field (must match company's field; "All in One" can choose any)
- Creation date is auto-generated

### 📄 Service Display
- Each service has a dedicated page showing:
  - Name
  - Description
  - Field
  - Price per hour
  - Creation date
  - Company (clickable to view profile)

- **Company profile** lists all its created services
- **Customer profile** lists all requested services

### 📊 Service Browsing
- Pages available:
  - All services (newest first)
  - Category-based service listings
  - Most requested services

---

## 📬 Service Request (Customer only)
- Requires:
  - Address
  - Service duration (in hours)
- After request:
  - Saved in customer profile
  - Displays:
    - Service name, field, provider company
    - Request date
    - Total cost (hours × hourly rate)

---

## 🧪 Functional Tests (What You Should Be Able To Do)

- [x] Register a new Customer (with required fields)
- [x] Register a new Company with "Electricity" as field
- [x] Field of work is validated from allowed list
- [x] Register both types of users independently
- [x] Error shown for duplicate username/email during registration
- [x] View Company profile after login (info visible, no password)
- [x] Company can create a service with price (e.g., 10.50)
- [x] New service appears in Company profile
- [x] View all created services
- [x] View services by category
- [x] Each service has its own detailed page
- [x] Customer profile shows correct info (no password)
- [x] Request a service for 2 hours
- [x] Input address and service time during request
- [x] Requested service appears in Customer profile
- [x] Total cost is calculated correctly (e.g., 2 × 10.50 = 21.00)
- [x] View most requested services page
- [x] Register "All in One" company and create service in any category
- [x] Create Painting service and request it multiple times
- [x] See most requested services update accordingly

---

## 📁 Tech Stack

- **Django v3.1.14**
- Python 3+
- HTML/CSS + Django Templates


---

## 🔄 Basic Commands

```bash
python3 manage.py runserver          # Start dev server
python3 manage.py startapp <name>   # Create new app
python3 manage.py makemigrations    # Generate DB migrations
python3 manage.py migrate           # Apply DB migrations
python3 manage.py createsuperuser   # Create admin user
