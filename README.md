# SAP CAP Bookshop Application

A bookshop application developed using the **SAP Cloud Application Programming Model (CAP)**, CDS, Node.js, and OData V4. The application manages books, authors, orders, and customer reviews, with business logic for stock validation, book discounts, and review rating validation.

A Python script integrates with the OData API to submit book reviews and calculate average ratings.

## Features

- **Book and Author Management:** Access book and author data through OData V4 services.
- **Discount Labels:** Apply a discount label to books with stock greater than 100.
- **Order Processing:** Validate available stock before processing orders.
- **Book Reviews:** Create reviews associated with individual books.
- **Rating Validation:** Accept only integer ratings between 1 and 5.
- **Python Integration:** Submit reviews through the OData V4 API using Python.
- **Average Rating Calculation:** Calculate the average rating for each book based on submitted reviews.

## Technologies Used

- **Backend:** Node.js, SAP CAP
- **Data Modeling:** CDS (Core Data Services)
- **API:** OData V4
- **Scripting:** Python 3
- **HTTP Client:** Python Requests
- **Development Tools:** Visual Studio Code, npm, Git, GitHub

## Project Structure

```text
Sap_Cap_project_1/
├── db/
│   └── schema.cds
├── srv/
│   ├── cat-service.cds
│   └── cat-service.js
├── post_review.py
├── package.json
└── README.md
```

*Note: The structure above is an example. Adjust filenames to match the actual files in your repository.*

## Prerequisites

Make sure the following tools are installed:

- Node.js and npm
- SAP CAP Development Kit (`@sap/cds-dk`)
- Python 3
- Python Requests library
- Visual Studio Code (recommended)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Sap_Cap_project_1
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Install Node.js Dependencies

```bash
npm install
```

If the SAP CAP Development Kit is not installed, install it using:

```bash
npm install -g @sap/cds-dk
```

Verify the installation:

```bash
cds --version
```

### 3. Install Python Dependencies

```bash
python -m pip install requests
```

## Running the Application

Start the CAP development server from the project root:

```bash
cds watch
```

The application is normally available at:

**http://localhost:4004**

Keep the server running while testing the API or submitting reviews.

## OData V4 Endpoints

| Endpoint | Description |
|---|---|
| `http://localhost:4004` | CAP application landing page |
| `/odata/v4/catalog/Books` | Retrieve books |
| `/odata/v4/catalog/Reviews` | Retrieve reviews |
| `/odata/v4/catalog/$metadata` | View OData service metadata |

Use the actual service paths displayed on the CAP application landing page if they differ.

## Review Rating Validation

The application validates review ratings before saving them.

| Rating | Expected Result |
|---|---|
| Integer from 1 to 5 | Accepted if all other data is valid |
| `0` or `6` | Rejected |
| Decimal such as `3.5` | Rejected |

### Example Review Request

**Method:** `POST`

**URL:**

```text
http://localhost:4004/odata/v4/catalog/Reviews
```

**Request Body:**

```json
{
  "rating": 5,
  "comment": "Excellent book",
  "book_ID": 1
}
```

A successful request typically returns `201 Created`.

Make sure the referenced book exists in the database and that the request matches the entity fields defined in your CDS model.

## Python Review Integration

With the CAP server running, open a second terminal in the project directory and execute:

```bash
python post_review.py
```

The script sends review requests through the OData V4 API and calculates average ratings for the reviews submitted during that execution.

### Example Output

```text
Review added for Book 1: 5/5
Review added for Book 1: 4/5
Review added for Book 2: 3/5

Average rating per book:
Book ID 1: 4.50/5
Book ID 2: 3.00/5
```

*The output above is an illustrative example. Actual results depend on the script, database records, and successful API requests.*

## Average Rating Calculation

For Book 1:

- Ratings: 5 and 4
- Average: (5 + 4) / 2
- **Average rating: 4.50/5**

For Book 2:

- Rating: 3
- Average: 3 / 1
- **Average rating: 3.00/5**

| Book ID | Number of Reviews | Average Rating |
|---|---:|---:|
| 1 | 2 | 4.50/5 |
| 2 | 1 | 3.00/5 |

These values illustrate the calculation using the example reviews.

## Troubleshooting

- **Port 4004 is already in use:** Stop the existing CAP server before restarting the application.
- **404 Not Found:** Verify the OData service path and confirm that the entity is exposed.
- **400 Bad Request:** Check the rating, request body, and required fields.
- **Python connection error:** Confirm that the CAP server is running and the API URL is correct.
- **Book association error:** Use a valid book ID retrieved from the Books endpoint.
- **Dependency errors:** Run `npm install` and verify that Python Requests is installed.

## Key Learning Outcomes

Through this project, I explored:

- SAP Cloud Application Programming Model fundamentals.
- CDS-based data modeling and entity associations.
- OData V4 endpoints and HTTP requests.
- Business logic and data validation in a CAP service.
- Python integration with backend APIs.
- Review aggregation and average rating calculations.

## Conclusion

This project demonstrates the development of a bookshop backend using SAP CAP, CDS, Node.js, and OData V4. It combines data modeling, business validations, order processing, and review management with Python-based API integration to calculate average book ratings.

