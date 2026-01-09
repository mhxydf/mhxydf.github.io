// 博客文章加载脚本

// 格式化日期用于排序
function parseDate(dateStr) {
    const match = dateStr.match(/(\d{4})年(\d{1,2})月(\d{1,2})日/);
    if (match) {
        const year = parseInt(match[1]);
        const month = parseInt(match[2]);
        const day = parseInt(match[3]);
        return new Date(year, month - 1, day);
    }
    return new Date(0);
}

// 渲染文章卡片（用于首页）
function renderPostCard(post) {
    return `
        <article class="post-card">
            <div class="post-meta">
                <span class="post-date">${post.date}</span>
                <span class="post-category">${post.category}</span>
            </div>
            <h2 class="post-title">
                <a href="posts/${post.filename}">${post.title}</a>
            </h2>
            <p class="post-excerpt">
                ${post.excerpt}
            </p>
            <a href="posts/${post.filename}" class="read-more">阅读更多 →</a>
        </article>
    `;
}

// 渲染归档项（用于归档页）
function renderArchiveItem(post) {
    return `
        <div class="archive-item">
            <h3><a href="posts/${post.filename}">${post.title}</a></h3>
            <div class="archive-meta">
                <span>${post.date}</span> | 
                <span>${post.category}</span>
            </div>
        </div>
    `;
}

// 加载并显示文章列表
async function loadPosts(containerId, renderFunction, sortByDate = true) {
    try {
        const response = await fetch('posts.json');
        if (!response.ok) {
            throw new Error('无法加载文章列表');
        }
        
        const posts = await response.json();
        
        // 按日期排序（最新的在前）
        if (sortByDate) {
            posts.sort((a, b) => {
                const dateA = parseDate(a.date);
                const dateB = parseDate(b.date);
                return dateB - dateA; // 降序
            });
        }
        
        // 渲染文章
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = posts.map(renderFunction).join('');
        } else {
            console.error(`找不到容器: ${containerId}`);
        }
    } catch (error) {
        console.error('加载文章失败:', error);
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = '<p style="text-align: center; color: #999;">加载文章列表失败，请稍后重试。</p>';
        }
    }
}

// 页面加载完成后自动加载文章
document.addEventListener('DOMContentLoaded', function() {
    // 检查当前页面类型并加载相应的内容
    const blogPostsContainer = document.getElementById('blog-posts');
    const archiveListContainer = document.getElementById('archive-list');
    
    if (blogPostsContainer) {
        // 首页：加载文章卡片
        loadPosts('blog-posts', renderPostCard, true);
    }
    
    if (archiveListContainer) {
        // 归档页：加载归档列表
        loadPosts('archive-list', renderArchiveItem, true);
    }
});

