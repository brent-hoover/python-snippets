BOOST_PYTHON_MODULE(rational)
{
  class_<boost::rational<int> >("int")
    ...
