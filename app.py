import src.weatherapp.test as weatherapp
import streamlit as st
import SessionState


def old_funct():
  '''
  #day = ['Saturday', 'Saturday Night']
  day = ['Sunday', 'Sunday Night']
  #day = ['Today', 'Tonight']

  print(f"{day}'s Forecast")
  for key in coords.keys():
    data = get_forecast_endpoint(coords[key])
    time.sleep(0.5)
    forecast = get_forecast(data['properties']['forecast'])
    forecast = list(filter(lambda x: x['name'] in day, forecast['properties']['periods']))
    print(f'{key}')
    print("Daytime:", wrap_text(forecast[0]['detailedForecast'], indent=' ' * 9))
    print("  Night:", wrap_text(forecast[1]['detailedForecast'], indent=' ' * 9))
    print('-' * 10)
    time.sleep(.5)

  print('Daytime = 6AM - 6PM local time')
  print('Night = 6PM - 6AM local time')
  '''

def main():
  new_loc = st.text_input('Location')
  session_state = SessionState.get(locs=[])
  if st.button('add') or new_loc:
    # process code here
    session_state.locs.append(new_loc)
  multiselect_filter = st.multiselect("custom filter", session_state.locs, default=session_state.locs)

  for loc in session_state.locs:
    st.text(weatherapp.get_longlat(loc))

if __name__ == '__main__':
  main()


