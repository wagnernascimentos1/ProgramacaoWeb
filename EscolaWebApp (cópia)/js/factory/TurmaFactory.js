// Turma - Factory
var turmaFactory = function($http) {

  var baseUrl = "http://127.0.0.1:5001";

  var _listar = function() {
    return $http.get(baseUrl+ "/turmas")
  };

  var _buscarPorId = function(id) {
    return $http.get(baseUrl+ "/turmas/" + encodeURI(id))
  };

  var _cadastrar = function(turma) {
    return $http.post(baseUrl + "/turma", turma)
  };

  var _atualizar = function(turma) {
    return $http.put(baseUrl+ "/turma/" + encodeURI(id), turma)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("turmaApi", turmaFactory);
