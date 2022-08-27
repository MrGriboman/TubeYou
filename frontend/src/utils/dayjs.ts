import dayjs from 'dayjs';

import relativeTime from 'dayjs/plugin/relativeTime';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import ru from 'dayjs/locale/ru';

dayjs.extend(customParseFormat);
dayjs.extend(relativeTime);
dayjs.locale(ru);

export default dayjs;
