import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import gtfs_kit as gk
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import pandas as pd
import geopandas as gpd

class GTFSAnalyzer:
    def __init__(self, master):
        self.master = master
        self.master.title("GTFS Analyzer")

        self.label = tk.Label(master, text="Carregue o arquivo GTFS zipado")
        self.label.pack()

        self.load_button = tk.Button(master, text="Carregar GTFS", command=self.load_gtfs)
        self.load_button.pack()

        self.analyze_button = tk.Button(master, text="Analisar Rotas", command=self.analyze_routes, state=tk.DISABLED)
        self.analyze_button.pack()

        self.visualize_button = tk.Button(master, text="Visualizar Cobertura", command=self.visualize_coverage, state=tk.DISABLED)
        self.visualize_button.pack()

        self.quit_button = tk.Button(master, text="Sair", command=master.quit)
        self.quit_button.pack()

        self.result_label = tk.Label(master, text="Resultados:")
        self.result_label.pack()

        self.result_text = tk.Text(master, height=15, width=50)
        self.result_text.pack()

        self.feed = None

    def load_gtfs(self):
        filepath = filedialog.askopenfilename(filetypes=[("Arquivos Zipados", "*.zip")])
        if filepath:
            try:
                self.feed = gk.read_feed(filepath, dist_units='km')
                messagebox.showinfo("Sucesso", "Arquivo GTFS carregado com sucesso!")
                self.analyze_button.config(state=tk.NORMAL)
                self.visualize_button.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao carregar GTFS: {e}")

    def analyze_routes(self):
        if self.feed is None:
            messagebox.showerror("Erro", "Nenhum arquivo GTFS carregado!")
            return

        trips = self.feed.trips
        stop_times = self.feed.stop_times

        frequency_analysis = (stop_times.groupby("trip_id")
                               .size()
                               .reset_index(name="stop_count")
                               .merge(trips, on="trip_id"))

        frequent_routes = (frequency_analysis.groupby("route_id")
                           .agg({"stop_count": "sum"})
                           .reset_index()
                           .rename(columns={"stop_count": "total_stops"}))

        frequent_routes = frequent_routes.sort_values("total_stops", ascending=False)
        top_routes = frequent_routes.head(10)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Top 10 Rotas Mais Frequentes:\n")
        self.result_text.insert(tk.END, top_routes.to_string(index=False))

    def visualize_coverage(self):
        if self.feed is None:
            messagebox.showerror("Erro", "Nenhum arquivo GTFS carregado!")
            return

        stops = self.feed.stops
        stops["geometry"] = stops.apply(lambda row: Point(row["stop_lon"], row["stop_lat"]), axis=1)
        gdf_stops = gpd.GeoDataFrame(stops, geometry="geometry")

        convex_hull = gdf_stops.unary_union.convex_hull

        plt.figure(figsize=(10, 8))
        gdf_stops.plot(ax=plt.gca(), color="blue", markersize=5, label="Paradas")
        x, y = convex_hull.exterior.xy
        plt.plot(x, y, color="red", label="Cobertura Convexa")
        plt.title("Cobertura de Rotas de Transporte Público")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GTFSAnalyzer(root)
    root.mainloop()
