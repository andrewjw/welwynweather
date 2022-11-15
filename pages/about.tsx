export default function Year(props: any) {
  let data = props.data;

  return (
    <>
    <h2>About</h2>

    <a href="http://www.flickr.com/photos/andrew_j_w/6246463884/"><img src="http://farm7.staticflickr.com/6163/6246463884_4edf183da8.jpg" style={{"float": "right", "marginBottom": "10px"}} /></a>
    <p>This website shows the weather data collected from my back garden in <a href="https://goo.gl/maps/HooffEZZJvbAHoMg8">Welwyn Garden City</a>.</p>

    <p>The weather station we use is one of the many WH080 models, and we read the data using <a href="https://github.com/jim-easterbrook/pywws">PyWWS</a>.
    It measures indoor and outdoor temperature and humidity, wind speed and direction, pressure and it has rain guage.</p>

    <p>The weather station used is not a scientific instrument and it has not be calibrated or properly mounted so that data should be taken with a grain of salt.</p>

    <p>On 12<sup>th</sup> April 2017 we moved about half a mile. The weather station was remounted so the stats before and after this date are not directly comparable.
    Temperature, pressure and rain should be reasonable close but there will be a significant discontinuity with wind.</p>

    <br style={{"clear": "both"}} />
  
    </>
  );
}
