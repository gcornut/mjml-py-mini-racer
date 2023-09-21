import mjml from 'mjml-browser';

/**
 * Convert JSON string serialization of the MJML format into HTML
 *
 * @param mjmlJSONString JSON string serialization of the MJML format
 * @return HTML
 */
export function mjml2html(mjmlJSONString) {
    return mjml(JSON.parse(mjmlJSONString));
}