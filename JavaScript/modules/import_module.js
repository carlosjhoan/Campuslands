//import {suma, PI} from './moduel_1.js';

import * as mod1 from './moduel_1.js';
import {PI as PI_2} from './module_only_pi.js'
import message from './default_export.js';
console.log(mod1.suma(2, 5));
console.log("PI" + mod1.PI);
console.log(mod1.r_2);
console.log(PI_2);
console.log(message());