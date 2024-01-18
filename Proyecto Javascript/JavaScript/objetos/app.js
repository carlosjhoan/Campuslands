
    import user from './json_prove.json' assert {type : 'json'}
    const json_file = user;
    let string_json = JSON.stringify(json_file);
    const parse_json = JSON.parse(string_json);
    let arr_json = Object.entries(parse_json); 
    const arr_new_user = [['nombre', 'Jhon Spitia'], ['edad', '27']]
    arr_json.push(arr_new_user );
    console.log(arr_json)
    string_json = JSON.stringify(Object.fromEntries(arr_json))
    console.log(string_json);
    
