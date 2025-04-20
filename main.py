from data_loading import load_data
from data_cleanup import check_missing_data
from eda import describe_data, aggregate_data
from visualization import plot_crossbar, plot_piechart

data_path = "./Train.csv"

data = load_data(data_path)

print(data.head(10))

check_missing_data(data)

# EDA
print(describe_data(data))
print(aggregate_data(data, "Prior_purchases", "Cost_of_the_Product"))
print(aggregate_data(data, "Prior_purchases", "Customer_rating"))

# Visuals
plot_crossbar(data, "Product_importance", "Reached.on.Time_Y.N")
plot_crossbar(data, "Warehouse_block", "Reached.on.Time_Y.N")
plot_piechart(data, "Warehouse_block")
plot_piechart(data, "Mode_of_Shipment")
plot_piechart(data, "Customer_rating")