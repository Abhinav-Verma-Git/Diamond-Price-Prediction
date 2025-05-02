
<h1>💎 Diamond Price Prediction</h1>

<p>This project implements a simple <strong>Linear Regression</strong> model to predict the price of diamonds based on features like carat and depth. The project includes data visualization, model training, performance evaluation, and a sample prediction.</p>

<h2>📁 Dataset</h2>
<p>The dataset used is <code>diamonds.csv</code>, which contains features such as:</p>
<ul>
  <li>carat</li>
  <li>cut</li>
  <li>color</li>
  <li>clarity</li>
  <li>depth</li>
  <li>table</li>
  <li>price</li>
  <li>x, y, z (dimensions)</li>
</ul>
<p><strong>Note:</strong> Only <code>carat</code> and <code>depth</code> are used as features in the model.</p>

<h2>🧰 Libraries Used</h2>
<ul>
  <li>numpy</li>
  <li>pandas</li>
  <li>matplotlib</li>
  <li>seaborn</li>
  <li>scikit-learn</li>
</ul>

<h2>📊 Exploratory Data Analysis (EDA)</h2>
<ol>
  <li><strong>Correlation Heatmap</strong> - Shows relationships between numeric features.</li>
  <li><strong>Scatter Plot</strong> - carat vs clarity.</li>
  <li><strong>Line Plot</strong> - Average price over carat.</li>
</ol>

<h2>📌 Workflow</h2>
<h3>1. Data Preparation</h3>
<ul>
  <li>Loaded <code>diamonds.csv</code></li>
  <li>Selected features: <code>carat</code>, <code>depth</code></li>
  <li>Target: <code>price</code></li>
  <li>Split dataset into train (80%) and test (20%)</li>
</ul>

<h3>2. Model Building</h3>
<p>Used <strong>Linear Regression</strong> from <code>sklearn</code>.</p>

<h3>3. Evaluation Metrics</h3>
<p>Model evaluated on:</p>
<ul>
  <li>R² Score</li>
  <li>MAE</li>
  <li>MSE</li>
  <li>RMSE</li>
</ul>

<h3>4. Visualization</h3>
<p>Includes an <strong>Actual vs Predicted Prices</strong> scatter plot.</p>

<h3>5. Prediction Example</h3>
<p>Predicts price for a diamond with:</p>
<ul>
  <li>carat = 0.3</li>
  <li>depth = 60</li>
</ul>

<h2>📈 Results (Sample Output)</h2>
<div class="highlight">
<pre>
Training Set Performance:
R² Score: 0.8507
MAE: 1006.58
MSE: 2376879.00
RMSE: 1541.71

Testing Set Performance:
R² Score: 0.8506
MAE: 1005.84
MSE: 2375577.92
RMSE: 1541.29

Prediction Example:
The price of the Diamond would be: 612.45
</pre>
</div>
<p><em>Note: These are example values. Actual results may vary depending on dataset version.</em></p>

<h2>🖼️ Sample Plots</h2>
<ul>
  <li>Correlation Heatmap</li>
  <li>Carat vs Clarity Scatter</li>
  <li>Carat vs Price Lineplot</li>
  <li>Actual vs Predicted Prices Scatter Plot</li>
</ul>

<h2>🚀 How to Run</h2>
<ol>
  <li>Clone this repository.</li>
  <li>Place <code>diamonds.csv</code> in the root directory.</li>
  <li>Run the script:
    <pre><code>python3 diamond_price_prediction.py</code></pre>
  </li>
</ol>

<h2>📌 Future Improvements</h2>
<ul>
  <li>Include more features like cut, clarity, color, x, y, z</li>
  <li>Try advanced models (Random Forest, XGBoost)</li>
  <li>Build a web UI for real-time predictions</li>
</ul>

<h2>📬 Contact</h2>
<p>For questions or collaboration, feel free to reach out!</p>

</body>
</html>
