#include <boost/python.hpp>
#include <boost/rational.hpp>
/* two specific conversion functions: rational to float and to str */
static double
as_float(boost::rational<int> const& self)
{
  return double(self.numerator()) / self.denominator();
}
static boost::python::object
as_str(boost::rational<int> const& self)
{
  using boost::python::str;
  if (self.denominator() == 1) return str(self.numerator());
  return str(self.numerator()) + "/" + str(self.denominator());
}
/* the 'rational' Python extension module, with just one class in it: */
BOOST_PYTHON_MODULE(rational)
{
  boost::python::class_<boost::rational<int> >("int")
    .def(boost::python::init<int, optional<int> >())
    .def("numerator", &boost::rational<int>::numerator)
    .def("denominator", &boost::rational<int>::denominator)
    .def("__float__", as_float)
    .def("__str__", as_str)
    .def(-self)
    .def(self + self)
    .def(self - self)
    .def(self * self)
    .def(self / self)
    .def(self + int())
    .def(self - int())
    .def(self * int())
    .def(self / int())
    .def(int() + self)
    .def(int() - self)
    .def(int() * self)
    .def(int() / self)
  ;
}
