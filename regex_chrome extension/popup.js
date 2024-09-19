function setPopupSize() {
  document.body.style.width = '800px'; // Increased width
  document.body.style.height = '600px';
}

document.addEventListener('DOMContentLoaded', function() {
  setPopupSize();
  const apiKeyForm = document.getElementById('api-key-form');
  const mainContent = document.getElementById('main-content');
  const apiKeyInput = document.getElementById('api-key-input');
  const saveApiKeyButton = document.getElementById('save-api-key');
  const regexInput = document.getElementById('regex-input');
  const getRegexButton = document.getElementById('get-regex');
  const resultDiv = document.getElementById('result');
  const loadingDiv = document.getElementById('loading');
  const progressInfo = document.getElementById('progress-info');

  // Check if API key exists
  chrome.storage.local.get(['openaiApiKey'], function(result) {
    if (!result.openaiApiKey) {
      apiKeyForm.style.display = 'block';
      mainContent.style.display = 'none';
    }
  });

  // Save API key
  saveApiKeyButton.addEventListener('click', function() {
    const apiKey = apiKeyInput.value.trim();
    if (apiKey) {
      chrome.storage.local.set({openaiApiKey: apiKey}, function() {
        apiKeyForm.style.display = 'none';
        mainContent.style.display = 'block';
      });
    }
  });

  // Get regex pattern
  getRegexButton.addEventListener('click', function() {
    const input = regexInput.value.trim();
    if (input) {
      loadingDiv.style.display = 'block';
      progressInfo.textContent = 'Sending request to OpenAI...';
      resultDiv.innerHTML = '';
      getRegexButton.disabled = true;

      chrome.runtime.sendMessage({action: 'getRegex', input: input}, function(response) {
        loadingDiv.style.display = 'none';
        getRegexButton.disabled = false;

        if (response.error) {
          resultDiv.innerHTML = `<p class="error">Error: ${response.error}</p>`;
        } else {
          try {
            // Parse the response if it's a string
            const parsedResponse = typeof response === 'string' ? JSON.parse(response) : response;
            
            let examplesHtml = '';
            if (Array.isArray(parsedResponse.examples)) {
              examplesHtml = parsedResponse.examples.map(example => `
                <div class="example">
                  <h4>${example.flavor} Example:</h4>
                  <pre><code>${example.pattern}</code></pre>
                  <p>Sample: ${example.sample}</p>
                  <p>${example.description}</p>
                </div>
              `).join('');
            } else {
              examplesHtml = '<p>No examples provided.</p>';
            }

            resultDiv.innerHTML = `
              <h3>Regex Pattern:</h3>
              <pre><code>${parsedResponse.regex || 'No pattern provided'}</code></pre>
              <h3>Explanation:</h3>
              <p>${parsedResponse.explanation || 'No explanation provided'}</p>
              <h3>Examples:</h3>
              ${examplesHtml}
            `;
          } catch (error) {
            resultDiv.innerHTML = `<p class="error">Error parsing response: ${error.message}</p>`;
            console.error('Full response:', response);
          }
        }
      });
    }
  });
});

function updateProgress(message) {
  document.getElementById('progress-info').textContent = message;
}
