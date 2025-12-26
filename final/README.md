# Rolex Watch Price Analysis - Final Project
## Data Analytics Course - Complete Analysis

---

## 📋 Project Overview

This project analyzes Rolex watch listings from Chrono24.com to understand pricing patterns, market trends, and factors affecting luxury watch values.

### Research Questions:
1. What factors most influence Rolex watch prices?
2. How do condition, materials, and documentation affect value?
3. Can we predict prices based on watch characteristics?
4. What market segments exist in the luxury watch market?

---

## 🎯 Project Requirements Met

### Minimum Requirements (8 points):
- ✅ **(1) Data Collection**: Web-scraped data from Chrono24.com
- ✅ **(2) Data Preparation**: Cleaning, feature engineering, outlier removal
- ✅ **(3) Database Storage**: PostgreSQL database with Docker
- ✅ **(4) Exploratory Data Analysis**: Rich graphical and statistical analysis
- ✅ **(5) Regression Modeling**: Linear regression and Random Forest
- ✅ **(6) Model Evaluation**: R-squared, RMSE, MAE metrics
- ✅ **(7) Interpretation**: Detailed analysis and business insights
- ✅ **(8) Materials Submission**: All notebooks and data included

### Additional Points (up to 5 points):
- ✅ **PostgreSQL Database** (not SQLite) - Docker Compose setup
- ✅ **Chi-squared Test** - Testing categorical variable relationships
- ✅ **ANOVA** - Price differences across conditions and materials
- ✅ **Correlation Analysis** - With p-values and significance tests
- ✅ **K-Means Clustering** - Market segmentation analysis
- ✅ **Geographic Visualization** - Interactive maps with Plotly/Folium

---

## 📁 Project Structure

```
final/
├── README.md                           # This file
├── docker-compose.yml                  # PostgreSQL database setup
├── requirements.txt                    # Python dependencies
├── .env.example                        # Environment variables template
│
├── chrono.csv                          # Raw scraped data
├── rolex_data_cleaned.csv             # Cleaned dataset
│
├── 01_data_preparation.ipynb          # Data cleaning & feature engineering
├── 02_database_storage.ipynb          # PostgreSQL setup & SQL queries
├── 03_exploratory_analysis.ipynb      # EDA with visualizations
├── 04_statistical_analysis.ipynb      # Chi-squared, ANOVA, Correlation
├── 05_regression_modeling.ipynb       # Price prediction models
└── 06_clustering_analysis.ipynb       # K-means market segmentation
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start PostgreSQL Database

```bash
# Start the database
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f postgres

# Stop the database
docker-compose down
```

### 3. Access pgAdmin (Optional)

- URL: http://localhost:5050
- Email: admin@rolex.local
- Password: admin

### 4. Run Notebooks in Order

Execute the notebooks sequentially:
1. `01_data_preparation.ipynb` - Cleans data and creates features
2. `02_database_storage.ipynb` - Loads data into PostgreSQL
3. `03_exploratory_analysis.ipynb` - Visual exploration
4. `04_statistical_analysis.ipynb` - Statistical tests
5. `05_regression_modeling.ipynb` - Price prediction
6. `06_clustering_analysis.ipynb` - Market segmentation

---

## 📊 Notebooks Description

### Notebook 1: Data Preparation
**Purpose**: Clean raw data and engineer features

**Key Tasks**:
- Import raw Chrono24 data
- Extract numeric values (price, year)
- Create categorical variables (condition, material)
- Generate binary features (has_box, has_papers)
- Extract geographic information
- Calculate watch age
- Remove outliers and duplicates

**Output**: `rolex_data_cleaned.csv`

---

### Notebook 2: Database Storage (PostgreSQL)
**Purpose**: Store data in PostgreSQL and perform SQL queries

**Key Tasks**:
- Connect to PostgreSQL via Docker
- Create properly structured tables
- Create indexes for performance
- Load cleaned data
- Execute complex SQL queries:
  - Aggregations and grouping
  - JOINs and CTEs
  - Window functions
  - Statistical calculations

**Technologies**: PostgreSQL 15, psycopg2, SQLAlchemy

---

### Notebook 3: Exploratory Data Analysis
**Purpose**: Visual and statistical exploration

**Key Visualizations**:
- Price distributions (histograms, box plots)
- Condition impact on price
- Material category analysis
- Age vs price relationships
- Geographic distribution
- Documentation impact
- Top models analysis
- Interactive Plotly charts

**Insights Generated**:
- Price patterns and distributions
- Key value drivers
- Market concentrations

---

### Notebook 4: Statistical Analysis
**Purpose**: Formal statistical testing with p-values

**Statistical Tests**:
1. **Correlation Analysis**
   - Pearson correlation between continuous variables
   - Significance testing (p-values)
   - Correlation heatmap

2. **Chi-Squared Test**
   - Test relationships between categorical variables
   - Condition vs Material category
   - Seller type vs Documentation
   - Interpretation with p-values

3. **ANOVA (Analysis of Variance)**
   - Price differences across condition categories
   - Price differences across materials
   - Post-hoc tests if significant
   - F-statistic and p-value interpretation

**Output**: Statistical evidence for variable relationships

---

### Notebook 5: Regression Modeling
**Purpose**: Predict watch prices using regression

**Models Implemented**:
1. **Simple Linear Regression**
   - Price vs single predictor
   - Model diagnostics

2. **Multiple Linear Regression**
   - Multiple predictors (age, material, condition, documentation)
   - Coefficient interpretation
   - Residual analysis

3. **Random Forest Regression**
   - Non-linear relationships
   - Feature importance
   - Better predictive performance

**Evaluation Metrics**:
- R-squared (coefficient of determination)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- Residual plots
- Predicted vs Actual plots

---

### Notebook 6: Clustering Analysis
**Purpose**: Segment the luxury watch market using K-means

**Key Tasks**:
- Feature selection and scaling
- Elbow method for optimal k
- K-means clustering (4 clusters)
- Cluster profiling and interpretation
- Visualization of clusters
- Business insights per segment

**Market Segments**:
- Ultra-luxury segment
- Premium modern segment
- Vintage collectors segment
- Entry-level luxury segment

---

## 🔑 Key Features

### Data Features Used:
- **Price** (target variable)
- **Age** (calculated from production year)
- **Condition Category** (New, Very Good, Good, Used, etc.)
- **Material Category** (Steel, Gold, Platinum, etc.)
- **Has Box** (binary)
- **Has Papers** (binary)
- **Has Complete Set** (binary)
- **Is Professional** (dealer vs private)
- **Country** (seller location)
- **Model** (watch model name)

### Engineered Features:
- Watch age from production year
- Documentation completeness
- Material categories from raw text
- Condition categories from descriptions
- Geographic groupings

---

## 📈 Key Findings

### Price Drivers:
1. **Material**: Precious metals (gold, platinum) command 2-3x premium over steel
2. **Condition**: New watches priced ~30-50% higher than used
3. **Documentation**: Complete set (box + papers) adds 15-25% to value
4. **Age**: Complex non-linear relationship - both very new and vintage command premiums
5. **Model**: Iconic models (Daytona, Submariner) have price premiums

### Statistical Significance:
- All major factors show p-values < 0.05 (statistically significant)
- Material category has strongest correlation with price
- ANOVA confirms significant price differences across groups

### Predictive Models:
- Random Forest outperforms linear regression
- R-squared: ~0.60-0.70 (models explain 60-70% of price variance)
- Most important features: material, age, model, condition

### Market Segments:
- **Segment 1**: Ultra-luxury (precious metals, perfect condition)
- **Segment 2**: Premium modern (recent, well-documented)
- **Segment 3**: Vintage collectors (older, variable condition)
- **Segment 4**: Entry-level (steel, basic documentation)

---

## 🗄️ Database Schema

### Table: watches

```sql
CREATE TABLE watches (
    id SERIAL PRIMARY KEY,
    web_scraper_order VARCHAR(50),
    brand VARCHAR(100),
    model VARCHAR(200),
    reference_number VARCHAR(100),
    movement_type VARCHAR(50),
    condition_category VARCHAR(50),
    seller_type VARCHAR(100),
    case_material VARCHAR(100),
    bracelet_material VARCHAR(100),
    material_category VARCHAR(50),
    country VARCHAR(100),
    city VARCHAR(100),
    price DECIMAL(12, 2),
    year INTEGER,
    age INTEGER,
    has_box INTEGER,
    has_papers INTEGER,
    has_complete_set INTEGER,
    is_professional INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Indexes for Performance:
- `idx_price` on price
- `idx_country` on country
- `idx_condition` on condition_category
- `idx_material` on material_category
- `idx_year` on year

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical graphics
- **Plotly** - Interactive visualizations
- **Folium** - Geographic maps
- **Scikit-learn** - Machine learning
- **SciPy** - Statistical tests
- **Statsmodels** - Regression analysis
- **PostgreSQL** - Database
- **Docker** - Containerization
- **SQLAlchemy** - ORM and database toolkit
- **psycopg2** - PostgreSQL adapter

---

## 📊 Sample SQL Queries

### Average Price by Condition:
```sql
SELECT
    condition_category,
    COUNT(*) as count,
    ROUND(AVG(price)::numeric, 2) as avg_price
FROM watches
GROUP BY condition_category
ORDER BY avg_price DESC;
```

### Top Countries:
```sql
SELECT
    country,
    COUNT(*) as num_listings,
    ROUND(AVG(price)::numeric, 2) as avg_price
FROM watches
GROUP BY country
ORDER BY num_listings DESC
LIMIT 10;
```

### Best Value Watches (Complex):
```sql
WITH avg_prices AS (
    SELECT
        material_category,
        AVG(price) as avg_mat_price
    FROM watches
    GROUP BY material_category
)
SELECT
    w.model,
    w.price,
    ap.avg_mat_price,
    ROUND(((w.price - ap.avg_mat_price) / ap.avg_mat_price * 100)::numeric, 2) as deviation_pct
FROM watches w
JOIN avg_prices ap ON w.material_category = ap.material_category
WHERE w.condition_category IN ('New', 'Very Good')
ORDER BY deviation_pct ASC
LIMIT 20;
```

---

## 📝 Notes

### Data Source:
- **Website**: Chrono24.com
- **Scraped**: Rolex watches only
- **Listings**: 50,000+ records
- **Date**: 2024

### Limitations:
- Data represents asking prices, not transaction prices
- Limited to Chrono24 marketplace
- Missing data for some variables
- Geographic bias toward European markets

### Future Improvements:
- Include additional brands for comparison
- Track prices over time for trend analysis
- Incorporate macro-economic indicators
- Add sentiment analysis of descriptions
- Compare multiple marketplaces

---

## 🎓 Academic Integrity

This project was completed for the Data Analytics course and demonstrates:
- Complete data pipeline (collection → analysis → modeling)
- Statistical rigor with p-values
- Multiple analytical approaches
- Professional documentation
- Reproducible research practices

---

## 📧 Contact

For questions about this project, please refer to the course materials or instructor.

---

## ⚖️ License

This project is for educational purposes only. The data is scraped from publicly available sources and used solely for academic analysis.

---

**Last Updated**: December 2024
