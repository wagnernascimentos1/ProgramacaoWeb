// Turno - Factory
var turnoFactory = function($http) {

  var baseUrl = "http://127.0.0.1:5001";

  var _listar = function() {
    return $http.get(baseUrl+ "/turnos")
  };

  var _buscarPorId = function(id) {
    return $http.get(baseUrl+ "/turnos/" + encodeURI(id))
  };

  var _cadastrar = function(turno) {
    return $http.post(baseUrl + "/turno", turno)
  };

  var _atualizar = function(turno) {
    return $http.put(baseUrl+ "/turno/" + encodeURI(id), turno)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("turnoApi", turnoFactory);
