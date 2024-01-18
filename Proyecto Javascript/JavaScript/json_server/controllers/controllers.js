import { post } from "./../models/post.js";
import { get } from "./../models/get.js";
import { put } from "./../models/put.js";
import { delet } from "./../models/delete.js";

import { llenarFormulario, llenarSelect } from "./../views/utils.js";

export function controlador(formu, event, entidad, elemformu) {
  const URL = "http://localhost:4000/";
  let url = "";
  
  const datos = formu !== null ? Object.fromEntries(new FormData(formu)) : null;
  const value = event.target.value;

  switch (value) {
    case "Agregar":
      url = URL + entidad;
      post(url, datos);
      formu.reset();
      break;
    case "CARGARSELECT":
    case "Buscar":
      url = `${URL}${entidad}/${datos !== null ? datos.id : ""}`;
      get(url, formu).then((data) => {
        // Utilizar los datos obtenidos
        if (formu !== null) llenarFormulario(formu, data);
        else if (value === "CARGARSELECT") llenarSelect(data, elemformu);
      });
      break;
    case "Modificar":
      url = URL + entidad + `/${datos.id}`;
      put(url, datos);
      //formu.reset
      break;
    case "Borrar":
      url = URL + entidad + `/${datos.id}`;
      delet(url);
      formu.reset;
      break;
  }
}