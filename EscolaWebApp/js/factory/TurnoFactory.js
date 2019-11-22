// Turno - Factory
var turnoFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/turnos")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/turnos/" + encodeURI(id))
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
