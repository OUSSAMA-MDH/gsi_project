# 🏭 Design Patterns in Python — Factory Method & Abstract Factory

This repository contains a complete implementation of two essential **Creational Design Patterns** in Python:

- **Factory Method**
- **Abstract Factory**

The project demonstrates how these patterns improve **modularity**, **scalability**, and **maintainability** when creating object families such as geometric shapes (Circle, Square, Triangle, Rectangle) in both **2D** and **3D**.

---

## 📌 Project Overview

This project is divided into two main parts:

### **1️⃣ Factory Method**
Includes:
- Code **without design pattern** (classic `if/elif` instantiation)
- **Simple Factory** implementation
- **Specialized Factories**:
  - `ShapeFactory_SCT` → Circle, Square, Triangle  
  - `ShapeFactory_SCR` → Circle, Square, Rectangle  
- **Factory Method Application** for account management (Manager, Seller, Visitor)

### **2️⃣ Abstract Factory**
Includes:
- Complete hierarchy of **2D shapes** (Circle2D, Square2D, Triangle2D, Rectangle2D)
- Complete hierarchy of **3D shapes**
- Abstract factory `ShapeFactory`
- Concrete factories:
  - `ShapeFactory2D`
  - `ShapeFactory3D`

---

## 📂 Project Structure

