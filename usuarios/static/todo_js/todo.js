function MostrarTipo_soli() {
    var SelectipoSoli = document.getElementById("id_tiposolicitud").value;
    var tipo_soliDiv = document.getElementById("tipo_soli");
    tipo_soliDiv.innerHTML = "";
    switch (SelectipoSoli) {
        case "1":
            tipo_soliDiv.innerHTML = `
            <label for="fecha_inicio">Fecha de Inicio</label><br>
                <input type="date" name="fecha_inicio" id="fecha_inicio"><br>
                <label for="archivo">Archivo</label><br>
                <input type="file" name="archivo" id="archivo"><br>
                        `;
        
            break;

        case "2":
            tipo_soliDiv.innerHTML = `
            <div class="col-sm-12" >
                <h6 class="modal-title">Programa de Formacion<h6>
                <select class="form-control" id="id_programaformacion" name="id_programaformacion"  title='' style='cursor:pointer;' >
                    <option></option>
                    {% for municipio in municipio %}
                        <option value="{{ municipio.id_programaformacion }}">{{ municipio.nombre }}</option>
                    {% endfor %}							
                </select>
            </div>
            `;
            break;
            case "3":
                tipo_soliDiv.innerHTML = `
                `;
            break;
            case "opcion4":
                tipo_soliDiv.innerHTML = `
            `;
        default: ` `
            break;
    }
}

