from flask import Flask, render_template
import data
from random import sample

app = Flask(__name__)


@app.route('/')
def main():
    # Choose 6 random id from tours dictionary
    random_tours_id = sample(data.tours.keys(), 6)
    # Create dictionary with 6 random tours for render at index.html
    random_tours = {idx: data.tours[idx] for idx in random_tours_id}
    return render_template('index.html', rand_tour=random_tours, departures=data.departures,
                           subtitle=data.subtitle, description=data.description)


@app.route('/departures/<departure>/')
def departures(departure):
    # Create a dictionary of tours from desired 'departure'
    filtered_tours = {tour_id: tour_info for tour_id, tour_info in data.tours.items()
                      if tour_info['departure'] == departure}
    # Get proper departure_name for render_template
    departure_name = data.departures[departure][3:]
    # Get lists of prices and nights quantity for filtered_tours
    prices = [tour_val['price'] for tour_val in filtered_tours.values()]
    nights = [tour_val['nights'] for tour_val in filtered_tours.values()]
    return render_template('departure.html', filt_tours=filtered_tours, departure_name=departure_name,
                           tours_prices=prices, tours_nights=nights, departures=data.departures)


@app.route('/tours/<id>/')
def tours(id):
    tour = data.tours[int(id)]
    return render_template('tour.html', tour=tour, departures=data.departures)


if __name__ == '__main__':
    app.run()
