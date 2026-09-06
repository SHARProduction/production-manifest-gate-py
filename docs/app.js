const allowedStages = new Set(['preproduction', 'production', 'postproduction', 'delivery']);
const allowedRights = new Set(['cleared', 'licensed', 'synthetic', 'unknown']);
const lint = (value) => {
  const errors = [];
  if (!value || typeof value !== 'object' || Array.isArray(value)) return ['manifest must be a JSON object'];
  for (const key of ['title', 'project', 'stage', 'rights_status']) if (typeof value[key] !== 'string' || !value[key].trim()) errors.push(`${key} is required`);
  if (value.stage && !allowedStages.has(value.stage)) errors.push('stage must be one of: preproduction, production, postproduction, delivery');
  if (value.rights_status && !allowedRights.has(value.rights_status)) errors.push('rights_status must be one of: cleared, licensed, synthetic, unknown');
  if (value.rights_status === 'unknown') errors.push('rights_status=unknown is not releasable');
  return errors;
};
const input = document.querySelector('#manifest');
const result = document.querySelector('#result');
document.querySelector('#check').addEventListener('click', () => {
  try {
    const errors = lint(JSON.parse(input.value));
    result.textContent = errors.length ? `BLOCKED\n- ${errors.join('\n- ')}` : 'PASS: manifest is releasable';
    result.dataset.ok = String(!errors.length);
  } catch (error) { result.textContent = `BLOCKED\n- invalid JSON: ${error.message}`; result.dataset.ok = 'false'; }
});
